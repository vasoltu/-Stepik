# рекурсивный поиск всех родителей для child из запросас проверкой не встречался ли он ранее в списке запросов
# на входе: словарь наследования ошибок, список ранее поступивших запросов, ребенок из очередного запроса
def get_ans(m_dict, spisok, child):
    global fl
    # нащли ребенок поступал ранее в качестве запроса (исключение ранее обрабатывали), выход из рекурсии fl = 1
    if child in spisok:
        fl = 1  # получен положительный результат
        return 1
    elif m_dict[child] == 'None':  # дошли до родителя, у которого нет прародителя, конец ветки, шаг назад
        return 0
    for element_of_child in m_dict[child]:  # бежит по списку родителей для очередного ребенка
        if element_of_child not in m_dict:  # если очередной родитель ребенка не содержится в ключах
            continue
        else:
            # если прародитель есть, запусти рекурсию, взяв в качестве child его очередного родителя
            get_ans(m_dict, spisok, element_of_child)


# Объявление переменных
class_nas = {}
spi_sok_zap = []
fl = 0
# Ввод исходных данных. Заполнени словаря.
# Потомок - ключ, Список родителей - значение
n = int(input())  # количество строк исходных данных
for i in range(n):
    stroka1 = input()
    ind = stroka1.find(':')
    if ind != -1:  # у класса есть родитель
        sr1 = stroka1[0:ind - 1]
        sr2 = stroka1[ind + 2:]
        spi_sok = sr2.split()
        class_nas.update({sr1: spi_sok})
    else:
        class_nas.update({stroka1: 'None'})

# Обработка поступающих запросов и внесение оредного запроа в список уже поступивших заппросов
m = int(input())  # количество запросов, которые надо обработать
for j in range(m):
    stroka2 = input()
    if stroka2 not in spi_sok_zap:
        get_ans(class_nas, spi_sok_zap, stroka2)
        if fl == 1:
            print(stroka2)
        spi_sok_zap.append(stroka2)
        # print(spi_sok_zap)
        fl = 0
    else:
        print(stroka2)
        continue
