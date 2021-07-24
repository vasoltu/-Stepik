str = ''     # 'Создание пустой стоки'
sumelent = 0
spisoknoc = []   # 'Создание пустого списка'
spisoknol = []       # 'Создание пустого списка'
while str != 'end':     # '1 цикл(заполнение списка и создание списка списков)'
    str = input()       # 'Ввод'
    if str == 'end':    # '1 условие(прерывание цикла)'
        break
    else:
        spisoknoc = str.split(' ')
        spisoknol.append(spisoknoc)

cr = len(spisoknoc)             # 'Длина (количество столбцов)'
cs = len(spisoknol)             # 'Длина (количество строк)'
i = 0
j = 0
for i in range(cs):      # '2 цикл(создание матрицы)'
    for j in range(cr):  # '3 цикл(создание матрицы)
        if i + 1 == cs and j + 1 != cr:    # '2 условие(последняя строка, но не последний столбец)'
            sumelent = int(spisoknol[i - 1][j]) + int(spisoknol[0][j]) + int(spisoknol[i][j - 1]) + int(spisoknol[i][j + 1])
            print(sumelent, end=' ')
        elif i + 1 == cs and j + 1 == cr:  # '3 условие(последняя строка, последний столбец)'
            sumelent = int(spisoknol[i - 1][j]) + int(spisoknol[0][j]) + int(spisoknol[i][j - 1]) + int(spisoknol[i][0])
            print(sumelent, end=' ')
        elif i < cs and j + 1 == cr:       # '4 условие(не последняя строка, но последний столбец)'
            sumelent = int(spisoknol[i - 1][j]) + int(spisoknol[i + 1][j]) + int(spisoknol[i][j - 1]) + int(spisoknol[i][0])
            print(sumelent, end=' ')
        elif i < cs and j + 1 != cr:       # '5 условие(не последняя строка, не последний столбец)'
            sumelent = int(spisoknol[i - 1][j]) + int(spisoknol[i + 1][j]) + int(spisoknol[i][j - 1]) + int(spisoknol[i][j + 1])
            print(sumelent, end=' ')

    print()
