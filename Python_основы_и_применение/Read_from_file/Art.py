import requests
import re
import json

# чтение из файлаб создание переменнных и регулярного выпажения
read = open('Test(a.n.)(вх.дн.).txt', 'r')
sp = []
sp_j = []
a = "https://api.artsy.net/api/artists/0"
# построчное чтение из файла и запись данных в список
for line in read:
    sp.append(line.rstrip())
# данные для получение токена
client_id = '60eab2d17b22ec86be28'
client_secret = '69c847e7f937cf294bab44220465dfc0'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком и цикл для работы с requests
for i in range(len(sp)):
    # генерация запрсоса
    req = re.sub('0', sp[i], a)
    r = requests.get(req, headers=headers)
    r.encoding = 'utf-8'
    # разбираем ответ сервера
    j = json.loads(r.text)
    sp_j.append(j['birthday'] + ' ' + j['sortable_name'])
sp_j.sort()
# построчный вывод имен художников
for j in range(len(sp_j)):
    print(sp_j[j][5:])
