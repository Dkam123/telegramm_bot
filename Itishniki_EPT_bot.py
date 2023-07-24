import telebot
import requests

TOKEN = '6024950997:AAFwHLkNrbthprcyd7yGd6h6A6qN_57izZ0'
WEATHER_API_KEY = 'YOUR_WEATHER_API_KEY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название своего города:')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    weather_data = get_weather_data(city)
    if weather_data:
        bot.send_message(message.chat.id, weather_data)
    else:
        bot.send_message(message.chat.id, 'Не удалось получить данные о погоде для указанного города.')


def get_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'  # Используем единицы измерения в метрической системе
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return f'Погода в городе {city.title()}:\nОписание: {weather_description}\nТемпература: {temperature}°C\nВлажность: {humidity}%'
    else:
        return None


bot.polling(none_stop=True)

# Hi
