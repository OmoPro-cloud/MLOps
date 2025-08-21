import requests

def get_weather(city, api_key):
  try:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
      print('Error fetching weather', data.get('message', 'Unknown error'))
      return
    temp_k = data['main']['temp']
    temp_c = temp_k - 273.15
    weather_description = data['weather'][0]['description']
    print(f'Weather in {city}: {weather_description}')
    print(f'Temperature: {temp_c:.2f}C')
    return 'Done'
  except Exception as e:
    print('Error fetching weather: ', e)

#Usage

city = input('Enter City:')
api_key = 'd445f540e455fccdf27aed42e74a6fd4'
weather = get_weather(city, api_key)
print(weather)

'''
Modify function to accept multiple cities in a loop.

Display humidity and wind speed in addition to temperature.

Handle cases where city name is invalid.
'''