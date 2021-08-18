  
# Weather API
import requests

def format_response(weather_data):
    try:
        city_name   = weather_data['name']
        country_name= weather_data['sys']['country'] # ***
        condition   = weather_data['weather'][0]['description']
        temperature = weather_data["main"]["temp"]
        icon_name   = weather_data["weather"][0]["icon"]

        weather_report = "City: %s \nCountry: %s \nCondition: %s \nTemperature(°F): %s" % (city_name, country_name, condition, temperature) # **
    except:
        weather_report = "server error 500"
        icon_name = ""
    return (weather_report, icon_name)

def weather_information(city_name):
    # get weather Information by calling openweather api
    weather_key = "e1b9e0b7aee9851b9984a26f3675878e"
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q" : city_name, "units" : "imperial"}
    response = requests.get(url, params)
    weather_data = response.json()
    # print(weather_data)

    weather_report = format_response(weather_data)
    return weather_report
print("Wellcome To My Weather Application. This Application Designe and Developed By Uzzal Chandra Boissha.")