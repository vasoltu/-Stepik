import requests
# 'Подключение библиотеки requests и подсчет количества строк'
url = requests.get('https://stepic.org/media/attachments/course67/3.6.2/870.txt')
# 'Подсчет количества строк'
text = url.text.splitlines()
print(url.text)
