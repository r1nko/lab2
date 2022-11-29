import requests
city = "Moscow,RU"
lat=7349585
lon=30303
appid = "6193672cc6f39f919dd076df3581055d"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
 params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print("Город:", city)
print("Видимость", data['visibility'])
print("Скорость ветра", data['wind']['speed'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
 params = { 'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("На неделю:")
for i in data['list']:
 print("Дата ", i['dt_txt'])
 print("Видимость ", i['visibility'])
 print("Скорость ветра ", i['wind']['speed'])
 print("____________________________")
