# Weatherapp

Weather Forecast and Recommendation
This project provides a weather forecast and recommendation based on the OpenWeatherMap API. It allows users to input a city and a desired date to get the forecast for that specific date and receive a recommendation based on the weather conditions.

Prerequisites
Before running the project, make sure you have the following:

Python 3.x installed on your machine
Required Python packages installed (requests, pprint, pyttsx3)

Getting Started

Clone the repository or download the project files.
Install the required packages by running the following command:
pip install requests pprint pyttsx3
Open the Python script file weather_forecast.py in a text editor.

Usage

Run the Python script weather_forecast.py using the following command:
python weather_forecast.py

Enter your city when prompted: 
Enter your city: 
Enter the desired date in the format YYYY-MM-DD when prompted: Enter the date (YYYY-MM-DD) for which you want the forecast: .
The script will fetch the weather forecast from the OpenWeatherMap API and display the forecast for the specified date, as well as a recommendation based on the weather conditions.

The recommendation will also be spoken out using text-to-speech.
Example:
Enter your city: London
Enter the date (YYYY-MM-DD) for which you want the forecast: 2023-06-06
Forecast for London on 2023-06-06:
Date: 2023-06-06 09:00:00, Temperature: 18.5°C, Wind Speed: 3.12 m/s, Feels Like: 17.9°C, Weather: Rain, Description: light rain
Date: 2023-06-06 12:00:00, Temperature: 20.3°C, Wind Speed: 3.62 m/s, Feels Like: 19.8°C, Weather: Rain, Description: light rain
Date: 2023-06-06 15:00:00, Temperature: 21.2°C, Wind Speed: 4.12 m/s, Feels Like: 20.7°C, Weather: Rain, Description: light rain
Date: 2023-06-06 18:00:00, Temperature: 19.8°C, Wind Speed: 4.42 m/s, Feels Like: 19.3°C, Weather: Rain, Description: moderate rain

Weather Recommendation: It's rainy at that time. Don't forget to carry an umbrella!

Acknowledgments
This project uses the OpenWeatherMap API for weather data.  
The text-to-speech functionality is provided by the pyttsx3 library.  
The requests library is used for making HTTP requests to the API.  
The pprint module is used for pretty-printing the forecast data.  




