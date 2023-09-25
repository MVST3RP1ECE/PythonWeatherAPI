import requests, json

url = "https://api.openweathermap.org/data/2.5/weather?"

payload = {
    "lat": "54.9358",
    "lon": "43.3235",
    "units": "C",
    "appid": "011db3d6d15ba9309e2eb66e2f215fa0"  # <-- Deafault API KEY   |   e92ec778e1d3f049afbc15cf745939cb <- Haunt
    # Нужно зарегаться на https://openweathermap.org/ , получить API ключ и ввести данные
}

res = requests.get(url, params=payload)
data = json.loads(res.text)

# print(data)
weather = data['weather'][0]

# print(weather.items())
# print(weather["main"], "+++")
# print(data["main"]["temp"])
with open("JSON.txt", "w") as _JSONTXT:
    json.dump(data, _JSONTXT, indent= 3)

def pars_weather(weatherType, timeRange, measurementUnits):
    if (weatherType in data) and (timeRange in data[weatherType].keys()):
        print(
            weatherType,
            ": ",
            data[weatherType][timeRange],
            measurementUnits
        )
    else:
        print(weatherType, ": ", "none")


# ---------------sys params ---------------
print( "--------------- sys params ---------------")
print("country: ", data["sys"]["country"])
print("City: ", data["name"])
print("ID:", data["id"])
print( "--------------- sys params ---------------")
# ---------------sys params ---------------
pars_weather("clouds", "all", "%")
pars_weather("rain", "3h", "mm")
print("humidity: ", data["main"]["humidity"])
pars_weather("snow", "3h", "mm")
print("temp: ", int(data["main"]["temp"] - 273.15),"°C\n")
print("desc: ", weather["description"])

# Огромный костыль, не знаю как ведут себя параметры rain/snow. Нужно писать функцию.