import requests

s_city ="Moscow,RU"
appid = "10a8021bb8240cc315aa0a94299268ea"
appid2 = "6787b9e7b5c761fadbdf77e8da6bb24b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Видимость:",data['visibility'])
print("Скорость ветра:",data['wind']['speed'])

resweek = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
             params={'q': s_city,'cnt' : 7, 'units': 'metric', 'lang': 'ru', 'APPID': appid2})
weekdata = resweek.json()
print(weekdata)

print("Город:", s_city)
for i in weekdata['list']:
            print("Дата:",i['dt_txt'],"Температура:", (i['main']['temp']))
            print("Дата:",i['dt_txt'],"Видимость:", i['visibility'])
            print("Дата:",i['dt_txt'],"Скорость ветра:",(i['wind']['speed']) )
            print("Дата:",i['dt_txt'], "Погодные условия:",i['weather'][0]['description'] )
            print(" ")








