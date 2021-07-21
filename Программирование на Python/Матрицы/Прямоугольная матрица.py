str = ''     # 'Создание пустой стоки'
b = 0
spstr = []   # 'Создание пустого списка'
a = []       # 'Создание пустого списка'
while str != 'end':     # '1 цикл(заполнение списка и создание списка списков)'
    str = input()       # 'Ввод'
    if str == 'end':    # '1 условие(прерывание цикла)'
        break
    else:
        spstr = str.split(' ')
        a.append(spstr)

cr = len(spstr)             # 'Длина (количество столбцов)'
cs = len(a)                 # 'Длина (количество строк)'
i = 0
j = 0
for i in range(cs):      # '2 цикл(создание матрицы)'
    for j in range(cr):  # '3 цикл(создание матрицы)
        if i + 1 == cs and j + 1 != cr:    # '2 условие(последняя строка, но не последний столбец)'
            b = int(a[i - 1][j]) + int(a[0][j]) + int(a[i][j - 1]) + int(a[i][j + 1])
            print(b, end=' ')
        elif i + 1 == cs and j + 1 == cr:  # '3 условие(последняя строка, последний столбец)'
            b = int(a[i - 1][j]) + int(a[0][j]) + int(a[i][j - 1]) + int(a[i][0])
            print(b, end=' ')
        elif i < cs and j + 1 == cr:       # '4 условие(не последняя строка, но последний столбец)'
            b = int(a[i - 1][j]) + int(a[i + 1][j]) + int(a[i][j - 1]) + int(a[i][0])
            print(b, end=' ')
        elif i < cs and j + 1 != cr:       # '5 условие(не последняя строка, не последний столбец)'
            b = int(a[i - 1][j]) + int(a[i + 1][j]) + int(a[i][j - 1]) + int(a[i][j + 1])
            print(b, end=' ')

    print()
