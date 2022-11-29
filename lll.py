import requests
city = "Moscow,RU"
appid = "42cb6d9ecb6e273b462cf6df5880f4cf"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
 params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
 params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data ['list']:
 print("Дата", i['dt_txt'])
 print("Температура:", '{0:+3.0f}'.format(i['main']['temp']))
 print("Погодные условия:", i['weather'][0]['description'])
 print("____________________________")