# import, чтение из файла, создание пустого словоря и списка для дальнейшего использования
import requests
import re
import json
read = open('Test(и.с.)(вх.дн.).txt', 'r')
sp = []
d_js = {}
d_py = {}
# построчное чтение из файла и запись данных в список
for line in read:
    sp.append(int(line))
# цикл для работы с requests
for i in range(len(sp)):
    # генерация запрсоса
    a = 'http://numbersapi.com/ /math?json=true'
    req = re.sub(' ', str(sp[i]), a)
    # запрос данных по адресу
    r = requests.get(req)
    d_js = r.text
    # преобразование объекта json в объект python
    d_py = json.loads(d_js)
    # получение значения по ключу 'found'
    rez = d_py['found']
    # проверка результата
    if rez:
        print('Interesting')
    elif not rez:
        print('Boring')
