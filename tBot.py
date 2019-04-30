#Made  by Stepan Kozurak
#https://github.com/dannycrief

import telebot
import pyowm

owm = pyowm.OWM('API')  # My API key for weather
bot = telebot.TeleBot("TOKEN")  #connection to Telegram bot, use @BotFather

@bot.message_handler(content_types=['text']) # get ONLY text from input
def send_echo(message):
    #bot.reply_to(message, message.text) this is for reply

    observation = owm.weather_at_place(message.text) #get location
    w = observation.get_weather()
    temp_now = w.get_temperature('celsius')["temp"] #temperature now
    temp_min = w.get_temperature('celsius')["temp_min"] #min temperature
    temp_max = w.get_temperature('celsius')["temp_max"] #max temperature

    answer = "In " + message.text + " " + str(temp_now) + " celsius now!\n"
    answer += "Max temperature in " + message.text + " will be " + str(temp_max) + " celsius!\n"
    answer += "Min temperature in " + message.text + " was " + str(temp_min) + " celsius!\n\n"

    #Wind
    wind_speed = w.get_wind()["speed"] # get wind speed in m/s
    wind_km = wind_speed * 3.6 #wind speed in km/h
    answer += "Wind speed: " + str(wind_speed) +  " m/s or " + str(round(wind_km, 3))+" km/h\n\n"

    #SMT for bot :)
    if temp_now < 10:
        answer += "It is so cold now, dress warmly!"
    elif temp_now < 20:
        answer += "It is not so cold, but be careful!"
    elif temp_now >= 20:
        answer += "It is so hot! Dress easier!"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)# start our bot..
