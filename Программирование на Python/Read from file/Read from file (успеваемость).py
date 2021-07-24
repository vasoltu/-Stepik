file = "dataset(вход)(успеваемость).txt"
spisok = []
for line in open(file, 'r'):  # 'Построчное чтение'
    sf = line.rstrip()
    spisok.append(sf.split(';'))

length = len(spisok)  # 'Длина списка'
sred_zn = 0
file = open('dataset(выход)(успеваемость).txt', 'w+')  # 'Запись инф. в файл'
for i in range(length):  # 'Цикл для прохода по списку'
    for j in range(1, 4):  # 'Цикл для прохода по списку'
        sred_zn = sred_zn + int(spisok[i][j])  # 'Счетчик среднего значения по строке'
        if j == 3:  # 'Условие для деления'
            sred_zn = sred_zn / 3  # 'Подсчет среднего значения по строке'
            print(sred_zn, file=file)  # 'Запись среднего значения по строке'
            sred_zn = 0
sred_zn = 0
for i in range(1, 4):  # 'Цикл для прохода по списку'
    for j in range(length):  # 'Цикл для прохода по списку'
        sred_zn = sred_zn + int(spisok[j][i])  # 'Счетчик среднего значения по столбцу'
        if j == length - 1:  # 'Условие для деления'
            sred_zn = sred_zn / length  # 'Подсчет среднего значения по столбцу'
            print(sred_zn, end=' ', file=file)  # 'Запись среднего значения по столбцу'
            sred_zn = 0
file.close()
