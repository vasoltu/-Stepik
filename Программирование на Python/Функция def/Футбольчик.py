def update_team(teams, team, count1, count2): # 'Функции(для обновления данных о команде в словаре)'
    if team not in teams:
        teams[team] = [0, 0, 0, 0, 0] 
    teams[team][0] += 1
    if int(count1) > int(count2):  # 'Победа'
        teams[team][1] += 1
        teams[team][4] += 3
    elif int(count1) == int(count2):  # 'Ничья'
        teams[team][2] += 1
        teams[team][4] += 1
    elif int(count1) < int(count2):  # 'Поражение'
        teams[team][3] += 1


teams = {}   # 'Создание пустого словоря'
lines_num = int(input())  # 'Ввод'
for _ in range(lines_num):
    line = input().split(';')  # 'Ввод'
    team1 = line[0]
    team2 = line[2]
    update_team(teams, team1, line[1], line[3])
    update_team(teams, team2, line[3], line[1])

for com in teams.keys():  # 'Вывод словаря'
    print(com + ":" + str(teams[com][0]), str(teams[com][1]), str(teams[com][2]), str(teams[com][3]),
          str(teams[com][4]))

