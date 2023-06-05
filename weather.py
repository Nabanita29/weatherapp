import requests
from pprint import pprint
import pyttsx3

def get_forecast(city):
    params = {
        'q': city,
        'appid': '3c1cb747915411442c58c8ba08353754',
        'units': 'metric'
    }
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    response = requests.get(url, params=params)
    return response.json()

def format_forecast(forecast):
    date_time = forecast['dt_txt']
    temperature = forecast['main']['temp']
    wind_speed = forecast['wind']['speed']
    feels_like = forecast['main']['feels_like']
    weather = forecast['weather'][0]['main']
    description = forecast['weather'][0]['description']
    print(f"Date: {date_time}, Temperature: {temperature}°C, Wind Speed: {wind_speed} m/s, Feels Like: {feels_like}°C, Weather: {weather}, Description: {description}")

def filter_forecast(forecast_data, desired_date):
    filtered_forecast = [forecast for forecast in forecast_data['list'] if forecast['dt_txt'].split()[0] == desired_date]
    return filtered_forecast

def get_weather_recommendation(city, desired_date):
    forecast_data = get_forecast(city)
    filtered_forecast = filter_forecast(forecast_data, desired_date)

    if filtered_forecast:
        print(f"Forecast for {city} on {desired_date}:")
        for forecast in filtered_forecast:
            format_forecast(forecast)
    else:
        print(f"No forecast available for {city} on {desired_date}.")

    # Recommendation based on weather condition
    recommendation = ""
    for forecast in filtered_forecast:
        weather_condition = forecast["weather"][0]["main"]
        temperature = forecast["main"]["temp"]

        if weather_condition == "Rain":
            recommendation = "It's rainy at that time. Don't forget to carry an umbrella!"
        elif weather_condition == "Clouds":
            recommendation = "It's cloudy at that time. Don't forget to carry an umbrella!"
        elif weather_condition == "Clear" and temperature > 30:
            recommendation = "It's sunny and hot at that time. Remember to carry an extra bottle of water!"
        else:
            recommendation = "Enjoy the day!"
        break  # Consider only the first forecast for the specified date

    # Text-to-speech
    engine = pyttsx3.init()
    engine.say(recommendation)
    engine.runAndWait()

    return recommendation

city = input('Enter your city: ')
desired_date = input("Enter the date (YYYY-MM-DD) for which you want the forecast: ")

recommendation = get_weather_recommendation(city, desired_date)
print("Weather Recommendation:", recommendation)
