import requests
# 'Получаем с помощью метода get первый файл'
cnt = 0
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
text = r.text
text1 = r.text.split(' ')
print(text1)
print(text1[0])
# 'Запускаем цикл для чтения множества файлов с помощью метода get'
while True:
    if text1[0] == 'We':
        print(text)
        break
    else:
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + text)
        cnt += 1
        print(cnt)
        text = r.text
        text1 = r.text.split(' ')
