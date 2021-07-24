file = "dataset(вход)(повтор слов).txt"
s = ''
for line in open(file, 'r'):  # 'Построчное чтение и склеивание в 1 строку'
    s = s + ' ' + line.rstrip()

sc = s.lower()  # 'Регистр'
spisok = sc.split()  # 'Перевод в список'
spisok.sort()  # 'Сортировка списка'
print(spisok)  # 'Печать списка'
length = len(spisok)  # 'Длина списка'
dict = {}    # 'Создать пустой словарь'
elem = spisok[0]
num = 1               # 'Номер очередного элемента списка'
count = 1               # 'Количество одинаковых элементов, стоящих подряд'

while num < length:
    if spisok[num] == elem:  # 'Считаем кол-во одинаковых элементов, стоящих подряд'
        count = count + 1
        num = num + 1
    else:           # 'Заносим в словарь'
        if count in dict:   # 'Добавляем в список по существующему ключу'
            dict[count] += [elem]
        else:       # 'Заносим новый ключ и начинаем формировать список'
            dict.update({count: [elem]})
        if num < length:
            elem = spisok[num]   # 'Запоминаем след. элемент исх. списка для подсчета вхождений'
            num = num + 1
            count = 1
if count >= 1:              # 'Запись инф. о последнем эл-те исх. списка'
    if count in dict:
        dict[count] += [elem]
    else:
        dict.update({count: [elem]})
all_key = list(dict.keys())  # 'Получение списка из всех ключей словаря'
len_all_key = len(all_key)
max_key = all_key[0]
for j in range(len_all_key):    # 'Поиск максимального ключа'
    if max_key < all_key[j]:
        max_key = all_key[j]
max_key_elem = dict[max_key]           # 'Список значений из словаря по максимальному ключу'
file = open('dataset(выход)(повтор слов).txt', 'w+')
print(max_key_elem[0], max_key, file=file)  # 'Запись инф. в файл'
file.close()
