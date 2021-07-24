file = open('dataset(вход)(распаковка строки).txt', 'r')  # 'Открытие файла для чтения'
stroka = file.read()  # 'Получение данных из файла'
print(stroka)
file.close()     # 'Закрытие файла'
file = open('dataset(выход)(распаковка строки).txt', 'w+')  # 'Открытие файла для записи'
length = len(stroka)
count = 1
letter = stroka[0]         # 'Хранение буквы для печати'
while count < length:     # 'Начало 1 цикла(до конца поданой строки)'
    stroka_int = ''   # 'Количество повторений буквы, записанное в виде строки'
    num = stroka[count]     # 'Хранение цифры'
    while '0' <= num <= '9':      # 'Начало 2 цикла(пока идут только цифры)'
        stroka_int += num
        count += 1   # 'Увеличения счетчика для прохода по строке'
        if count < length:      # 'Условие 1(запоминаем новую цифру)'
            num = stroka[count]
        else:
            break
    for j in range(int(stroka_int)):    # 'Начало 3 цикла(запись в файл результата)'
        print(letter, end='', file=file)

    if count < length:         # 'Условие 2()'
        letter = stroka[count]      # 'Запоминаем новый элемент для печати'
        count += 1
file.close()
