file = "dataset(вход)(успеваемость).txt"
spisok = []
for line in open(file, 'r'):  # 'Построчное чтение'
    sf = line.rstrip()
    spisok.append(sf.split(';'))

ln = len(spisok)  # 'Длина списка'
sr = 0
file = open('dataset(выход)(успеваемость).txt', 'w+')  # 'Запись инф. в файл'
for i in range(ln):  # 'Цикл для прохода по списку'
    for j in range(1, 4):  # 'Цикл для прохода по списку'
        sr = sr + int(spisok[i][j])  # 'Счетчик среднего значения по строке'
        if j == 3:  # 'Условие для деления'
            sr = sr / 3  # 'Подсчет среднего значения по строке'
            print(sr, file=file)  # 'Запись среднего значения по строке'
            sr = 0
sr = 0
for i in range(1, 4):  # 'Цикл для прохода по списку'
    for j in range(ln):  # 'Цикл для прохода по списку'
        sr = sr + int(spisok[j][i])  # 'Счетчик среднего значения по столбцу'
        if j == ln - 1:  # 'Условие для деления'
            sr = sr / ln  # 'Подсчет среднего значения по столбцу'
            print(sr, end=' ', file=file)  # 'Запись среднего значения по столбцу'
            sr = 0
file.close()
