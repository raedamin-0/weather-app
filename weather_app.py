"""
Weather App - My first Python project
"""

# Import the 'typing' library for type hints
from typing import Dict, Optional, Any

# Import the 'requests' library
import requests

# Import os for environment variables
import os

# Import dotenv to load .env file with API key
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
# If not found, it will be empty string (you'll need to set it)
API_KEY: str = os.getenv("WEATHER_API_KEY", "")

# Define the base URL for weather API
BASE_URL: str = "http://api.weatherapi.com/v1/current.json"

def get_weather(city_name: str) -> Any:
    """
    Get the weather data for a given city.
    Arguments:
        city_name (str): Name of city to get weather for
        
    Returns:
        dict: Weather data in JSON format, or None if error
    """
   
    # Build the URL
    # Format: BASE_URL + "?key=" + API_KEY + "&q=" + city_name
    url: str = f"{BASE_URL}?key={API_KEY}&q={city_name}"

    # Make the request
    # Store the response in a variable called response
    response: requests.Response = requests.get(url)

    # Check if successful
    # Check: response.status_code == 200
    # If successful, return response.json()
    # If not, print an error message and return None
    if response.status_code == 200:
        return response.json()
        
    # Print more detailed error information for any API key failures or other failures
    if response.status_code == 403:
        print("Error 403: Forbidden - Check your API key in .env file")
    elif response.status_code == 401:
        print("Error 401: Unauthorized - Invalid API key")
    else:
        print(f"Error: {response.status_code}")
    return None

def display_weather(weather_data: Dict[str, Any]) -> None:
    """
    Display weather information in a readable format.
    
    Arguments:
        weather_data (dict): The weather data from the API
    """
 
    # Extract and display information
    # The weather_data is a dictionary, like a JSON object
    city: str = weather_data['location']['name']
    country: str = weather_data['location']['country']
    temp_f: float = weather_data['current']['temp_f']
    temp_c: float = weather_data['current']['temp_c']
    feelslike_f: float = weather_data['current']['feelslike_f']
    feelslike_c: float = weather_data['current']['feelslike_c']
    condition: str = weather_data['current']['condition']['text']
    last_updated: str = weather_data['current']['last_updated']    

    # Printing the information
    print(f"""Weather in {city}, {country}:
Temperature (°F): {temp_f}°F
Temperature (°C): {temp_c}°C
Feels like (°F): {feelslike_f}°F
Feels like (°C): {feelslike_c}°C
Conditions: {condition}
Last updated: {last_updated}""")

def main() -> None:
    """
    Main function -- where the program starts.
    """

    print("Welcome to the Weather App!")
    print("-" * 40)

    # Ask the user for a city name and store it in a variable
    city: str = input("Enter city name: ")
    # Call get_weather() with the city name and store the result in a variable
    weather_data: Optional[Dict[str, Any]] = get_weather(city)
    # Check if weather_data is not None
    # If not, call display_weather(weather_data)
    # If yes, print a friendly error message
    if weather_data is not None:
        display_weather(weather_data)


# Run main function when script is executed
if __name__ == "__main__":
    main()
