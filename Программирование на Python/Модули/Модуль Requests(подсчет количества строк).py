import requests
# 'Подключение библиотеки requests и подсчет количества строк'
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/870.txt')
# 'Подсчет количества строк'
text = r.text.splitlines()
print(r.text)
