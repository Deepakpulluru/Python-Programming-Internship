import http.client
import json

def get_weather(api_key, city_name):
    # Create a connection to the OpenWeatherMap API server
    conn = http.client.HTTPConnection("api.openweathermap.org")
    
    # Build the complete URL with the API key and city name
    url = f"/data/2.5/weather?appid={api_key}&q={city_name}"
    
    # Make the GET request
    conn.request("GET", url)
    
    # Get the response
    response = conn.getresponse()
    
    # Read the response data
    data = response.read()
    
    # Decode the data from bytes to a string and then parse it as JSON
    weather_data = json.loads(data.decode("utf-8"))
    
    # Check if the city is found (cod 200 means success)
    if weather_data["cod"] == 200:
        # Get the main data
        main_data = weather_data["main"]
        
        # Extract temperature, pressure, and humidity
        current_temperature = main_data["temp"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        
        # Get the weather description
        weather_description = weather_data["weather"][0]["description"]
        
        # Print the weather information
        print(f"Temperature (in Kelvin): {current_temperature}")
        print(f"Atmospheric pressure (in hPa): {current_pressure}")
        print(f"Humidity (in percentage): {current_humidity}")
        print(f"Weather description: {weather_description}")
    else:
        print("City Not Found")

# Replace 'Your_API_Key' with your actual API key
api_key = "Your_API_Key"

# Input city name from the user
city_name = input("Enter city name: ")

# Call the get_weather function
get_weather(api_key, city_name)
