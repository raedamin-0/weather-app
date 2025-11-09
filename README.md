# Weather App 🌤️

My first Python project - a simple weather application!

## The function of this project:
Fetching and displaying current weather information for any given city using the WeatherAPI.

## Setup instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd weather-app
   ```

2. **Install dependencies as needed**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Sign up and get a free API key from [WeatherAPI.com](https://www.weatherapi.com/)
   - Create a `.env` file in the project root:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```
   - Or set it as an environment variable:
     - Windows: `set WEATHER_API_KEY=your_api_key_here`
     - Linux/Mac: `export WEATHER_API_KEY=your_api_key_here`

4. **Run the app**
   ```bash
   python weather_app.py
   ```

## How to use
1. Run the script
2. Enter city name when prompted
3. View the weather information that has been outputted

## What I learned
- Working with APIs
- Making HTTP requests with the 'requests library'
- Parsing JSON data obtained from an HTTP request
- Handling user input
- Error handling
- Utilization of type hints in Python
- How a leaked API key can lead to some really severe security flaws in a program
- Using the 'os' and 'python-dotenv' libary and environment variables for maintaining security (mainly for the API key)

