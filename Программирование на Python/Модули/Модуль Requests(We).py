import requests
# 'Получаем с помощью метода get первый файл'
count = 0
url = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
text = url.text
text1 = url.text.split(' ')
print(text1)
print(text1[0])
# 'Запускаем цикл для чтения множества файлов с помощью метода get'
while True:
    if text1[0] == 'We':
        print(text)
        break
    else:
        url = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + text)
        count += 1
        print(count)
        text = url.text
        text1 = url.text.split(' ')
