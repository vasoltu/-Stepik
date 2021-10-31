import requests
import re

sp1 = []
sp2 = []
# шаблон для поиска адреса страницы
a = r'https.*html'
# адрес 1 документа
s1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# адрес 2 документа
s2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
r = requests.get(s1)  # получение данных со страницы s1
rez1 = re.findall(a, r.text)  # формирование списка адресов страниц, содержащихся в тексте страницы s1
sp1 = rez1  #
for j in range(len(sp1)):
    rr = requests.get(sp1[j])  # получение данных с каждой страницы из списка sp1
    rez2 = re.findall(a, rr.text)
    sp2 += rez2
if s2 in sp2:
    print('Yes')
else:
    print('No')


