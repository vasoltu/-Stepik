class_dict = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0], 8: [0, 0], 9: [0, 0],
              10: [0, 0], 11: [0, 0], }
file = "dataset(вход)(рост).txt"
stroka_input = ''
for line in open(file, 'r'):                    # 'Построчное чтение из файла'
    stroka_input = line.rstrip()                   # 'Считали строку'
    lst_input = stroka_input.split('\t')           # 'Преобразовали в список по символу табуляции'
    k = int(lst_input[0])
    rost = int(lst_input[2])
    class_dict[k][0] = class_dict[k][0] + rost  # 'Прибавили рост в нужный класс по ключу'
    class_dict[k][1] = class_dict[k][1] + 1     # 'Увеличили счетчик класса'
for key in class_dict:
    if class_dict[key][1] != 0:                 # 'В словаре присутствует инф. о росте'
        print(key, class_dict[key][0] / class_dict[key][1])
    else:
        print(key, '-')
