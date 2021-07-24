number_of_lines = input()    # 'Ввод'
stroka = ''         # 'Создание пустой стоки'
dict = {}      # 'Создание пустого словоря'
for j in range(int(number_of_lines)):    # '1 цикл(заполнение словаря)'
    stroka = input()            # 'Ввод'
    spisok = stroka.split(';')      # 'Создание списка'
    key_team1 = spisok[0]              # 'Условия для 1 команды'
    if key_team1 in dict:          # '1 условие(наличие ключа в словаре)'
        dict[key_team1][0] = dict[key_team1][0] + 1
        if int(spisok[1]) > int(spisok[3]):      # '1.1 условие(победа)'
            dict[key_team1][1] = dict[key_team1][1] + 1
            dict[key_team1][4] = dict[key_team1][4] + 3
        elif int(spisok[1]) == int(spisok[3]):   # '1.2 условие(ничья)'
            dict[key_team1][2] = dict[key_team1][2] + 1
            dict[key_team1][4] = dict[key_team1][4] + 1
        elif int(spisok[1]) < int(spisok[3]):    # '1.3 условие(поражение)'
            dict[key_team1][3] = dict[key_team1][3] + 1
    else:                                # '2 условие(не наличие ключа в словаре)'
        dict.update({key_team1: [1, 0, 0, 0, 0]})
        if int(spisok[1]) > int(spisok[3]):      # '2.1 условие(победа)'
            dict[key_team1][1] = dict[key_team1][1] + 1
            dict[key_team1][4] = dict[key_team1][4] + 3
        elif int(spisok[1]) == int(spisok[3]):   # '2.2 условие(ничья)'
            dict[key_team1][2] = dict[key_team1][2] + 1
            dict[key_team1][4] = dict[key_team1][4] + 1
        elif int(spisok[1]) < int(spisok[3]):    # '2.3 условие(поражение)'
            dict[key_team1][3] = dict[key_team1][3] + 1

    key_team2 = spisok[2]                           # 'Условия для 2 команды'
    if key_team2 in dict:                       # '1 условие(наличие ключа в словаре'
        dict[key_team2][0] = dict[key_team2][0] + 1
        if int(spisok[3]) > int(spisok[1]):      # '1.1 условие(победа)'
            dict[key_team2][1] = dict[key_team2][1] + 1
            dict[key_team2][4] = dict[key_team2][4] + 3
        elif int(spisok[3]) == int(spisok[1]):   # '1.2 условие(ничья)'
            dict[key_team2][2] = dict[key_team2][2] + 1
            dict[key_team2][4] = dict[key_team2][4] + 1
        elif int(spisok[3]) < int(spisok[1]):    # '1.3 условие(поражение)'
            dict[key_team2][3] = dict[key_team2][3] + 1
    else:                                # '2 условие(не наличие ключа в словаре)'
        dict.update({key_team2: [1, 0, 0, 0, 0]})
        if int(spisok[3]) > int(spisok[1]):      # '2.1 условие(победа)'
            dict[key_team2][1] = dict[key_team2][1] + 1
            dict[key_team2][4] = dict[key_team2][4] + 3
        elif int(spisok[3]) == int(spisok[1]):   # '2.2 условие(ничья)'
            dict[key_team2][2] = dict[key_team2][2] + 1
            dict[key_team2][4] = dict[key_team2][4] + 1
        elif int(spisok[3]) < int(spisok[1]):    # '2.3 условие(поражение)'
            dict[key_team2][3] = dict[key_team2][3] + 1

for com in dict.keys():                  # '2 цикл(вывод словаря)'
    print(com + ":" + str(dict[com][0]), str(dict[com][1]), str(dict[com][2]), str(dict[com][3]), str(dict[com][4]))
