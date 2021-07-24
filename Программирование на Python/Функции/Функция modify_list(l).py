def modify_list(lst):          # 'Создание функции'
    spisok = len(lst)
    i = 0
    while i < spisok:              # '1 цикл(проход списка)'
        if lst[i] % 2 != 0:    # '1 условие(нечетное число, удалить из списка)'
            del lst[i]
            spisok = spisok - 1
        elif lst[i] % 2 == 0:  # '2 условие(четное число, разделить на 2)'
            lst[i] = lst[i] // 2
            i = i + 1


lst = [10, 5, 8, 3]
modify_list(lst)    # 'Вызов функции'
