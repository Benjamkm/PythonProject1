import requests

city = input("Enter municipality name: ")

api_key = "apikey1"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if hasattr(response, "raise_for_status"):
        response.raise_for_status()

    data = response.json()

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather: {description}")
    print(f"Temperature: {temperature} Celsius")

except requests.exceptions.HTTPError:
    print("Error: Could not retrieve weather data")

except requests.exceptions.RequestException:
    print("Error: Network problem")

except KeyError:
    print("Error: Unexpected response format")

