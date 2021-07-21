n = input()    # 'Ввод'
s = ''         # 'Создание пустой стоки'
dict = {}      # 'Создание пустого словоря'
for j in range(int(n)):    # '1 цикл(заполнение словаря)'
    s = input()            # 'Ввод'
    sp = s.split(';')      # 'Создание списка'
    k = sp[0]              # 'Условия для 1 команды'
    if k in dict:          # '1 условие(наличие ключа в словаре)'
        dict[k][0] = dict[k][0] + 1
        if int(sp[1]) > int(sp[3]):      # '1.1 условие(победа)'
            dict[k][1] = dict[k][1] + 1
            dict[k][4] = dict[k][4] + 3
        elif int(sp[1]) == int(sp[3]):   # '1.2 условие(ничья)'
            dict[k][2] = dict[k][2] + 1
            dict[k][4] = dict[k][4] + 1
        elif int(sp[1]) < int(sp[3]):    # '1.3 условие(поражение)'
            dict[k][3] = dict[k][3] + 1
    else:                                # '2 условие(не наличие ключа в словаре)'
        dict.update({k: [1, 0, 0, 0, 0]})
        if int(sp[1]) > int(sp[3]):      # '2.1 условие(победа)'
            dict[k][1] = dict[k][1] + 1
            dict[k][4] = dict[k][4] + 3
        elif int(sp[1]) == int(sp[3]):   # '2.2 условие(ничья)'
            dict[k][2] = dict[k][2] + 1
            dict[k][4] = dict[k][4] + 1
        elif int(sp[1]) < int(sp[3]):    # '2.3 условие(поражение)'
            dict[k][3] = dict[k][3] + 1

    k1 = sp[2]                           # 'Условия для 2 команды'
    if k1 in dict:                       # '1 условие(наличие ключа в словаре'
        dict[k1][0] = dict[k1][0] + 1
        if int(sp[3]) > int(sp[1]):      # '1.1 условие(победа)'
            dict[k1][1] = dict[k1][1] + 1
            dict[k1][4] = dict[k1][4] + 3
        elif int(sp[3]) == int(sp[1]):   # '1.2 условие(ничья)'
            dict[k1][2] = dict[k1][2] + 1
            dict[k1][4] = dict[k1][4] + 1
        elif int(sp[3]) < int(sp[1]):    # '1.3 условие(поражение)'
            dict[k1][3] = dict[k1][3] + 1
    else:                                # '2 условие(не наличие ключа в словаре)'
        dict.update({k1: [1, 0, 0, 0, 0]})
        if int(sp[3]) > int(sp[1]):      # '2.1 условие(победа)'
            dict[k1][1] = dict[k1][1] + 1
            dict[k1][4] = dict[k1][4] + 3
        elif int(sp[3]) == int(sp[1]):   # '2.2 условие(ничья)'
            dict[k1][2] = dict[k1][2] + 1
            dict[k1][4] = dict[k1][4] + 1
        elif int(sp[3]) < int(sp[1]):    # '2.3 условие(поражение)'
            dict[k1][3] = dict[k1][3] + 1

for com in dict.keys():                  # '2 цикл(вывод словаря)'
    print(com + ":" + str(dict[com][0]), str(dict[com][1]), str(dict[com][2]), str(dict[com][3]), str(dict[com][4]))
