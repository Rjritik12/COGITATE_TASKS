import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    data = get_weather(city, api_key)
    if data["cod"]!= "404":
        main_data = data["main"]
        temperature = main_data["temp"] - 273.15 # Convert Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]
        print(f"Temperature : {temperature:.2f}°C")
        print(f"Atmospheric Pressure : {pressure} hPa")
        print(f"Humidity : {humidity}%")
        print(f"Weather Description : {weather_description}")
    else:
        print("City not found!")

if __name__ == "__main__":
    main()