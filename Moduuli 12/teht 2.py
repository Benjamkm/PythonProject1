import requests

city = input("Enter municipality name: ")

api_key = "apikey1"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather: {description}")
    print(f"Temperature: {temperature} Celsius")
else:
    print("Error: Could not retrieve weather data")