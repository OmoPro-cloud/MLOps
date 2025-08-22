import requests


'''
NEW: if an HTTP response is 200, then your request has succeeded.
If it's response is a 404, then the source couldn't be found.
A response of 500 indicates a server error
'''



#write a function that will take an input(city) from the user and return its current weather

def get_weather(city, api_key):
    """Fetch and return weather info dict for the city, or None on error."""
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f'Error fetching weather for "{city}":', data.get('message', 'Unknown error'))
            return None

        return {
            'city': city,
            'description': data['weather'][0]['description'],
            'temp_c': data['main']['temp'] - 273.15
        }
    except requests.RequestException as e:
        print('Error fetching weather (network issue):', e)
        return None
    except Exception as e:
        print('Unexpected error:', e)
        return None

def main(api_key):
    while True:
        city = input('Enter a city (or type "bye" to quit): ').strip()
        if city.lower() == 'bye':
            print('Goodbye!')
            break

        weather = get_weather(city, api_key)
        if weather:
            print(f"Weather in {weather['city']}: {weather['description']}")
            print(f"Temperature: {weather['temp_c']:.2f}°C")
        else:
            print('Please try again.')

if __name__ == '__main__':
    api_key = '6162d674c0d3ce291204035f9a8ce1e7'
    main(api_key)

#practice