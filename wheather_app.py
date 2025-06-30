import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = f"{base_url}appid={api_key}&q={city_name}&units=metric"

    response = requests.get(full_url)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]
        sys = data["sys"]


        print(f"City:{data['name']},{sys['country']}")
        print(f"Temperature:{main['temp']}°C")
        print(f"Feels like:{main['feels_like']}°C")
        print(f"Humidity:{main['humidity']}%")
        print(f"Pressure:{main['pressure']}hPa")
        print(f"Weather:{weather['description'].capitalize()}")
    else:
        print("City not found or API error")

def main():
    api_key = "4548a8863d9ea88a3ae410074644c7ae"
    city_name = input("Enter city name:")
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()
