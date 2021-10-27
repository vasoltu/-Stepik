# ввод исходных данных. Создание словаря
# потомок - ключ, список родителей - значение
def create_dict(m_dict, inp_str):
    spi_sok = []
    ind = inp_str.find(':')
    if ind != -1:  # у класса есть родитель
        sr1 = stroka1[0:ind - 1]
        sr2 = stroka1[ind + 2:]
        spi_sok = sr2.split()
        m_dict.update({sr1: spi_sok})
    else:
        m_dict.update({stroka1: 'None'})


# рекурсивный поиск родителя из запроса в списках  родмтелей (прародмтелей) для child из запроса
def get_ans(m_dict, parent, child):
    global fl
    if m_dict[child] == 'None':  # дошли до родителя, у которого нет прародителя, конец ветки, шаг назад
        return 0
    else:
        # нащли родителя из запроса в списке родителей очередного ребенка, выход из рекурсии fl = 1
        if child in m_dict and parent in m_dict[child]:
            fl = 1  # получен положительный результат
            return 1
        for element_of_child in m_dict[child]:  # бежит по списку родителей для очередного ребенка
            if element_of_child not in m_dict:  # если у родмтеля не праводителя, пропусти
                continue
            else:
                # если прародитель есть, запусти рекурсию, взяв в качестве child его очередного родителя
                get_ans(m_dict, parent, element_of_child)


# Основная программа
# объявление переменных
cla_ss = {}  # словарь для хранения данных о наследовании
requests = []  # хранит родмтеля и ребенка из очередного запроса
fl = 0  # хранит результат поиска

# ввод исходных данных
n = int(input())  # к-во строк, описывающих наследование классов
for i in range(n):
    stroka1 = input()
    create_dict(cla_ss, stroka1)  # занесение данных в словарь из очередной строки

k = int(input())  # к-во запросов
for j in range(k):
    # очистим флаг перед очередным использованием
    fl = 0
    requests = input()
    requests_sp = requests.split()
    if requests_sp[0] == requests_sp[1]:  # A=B
        print('Yes', requests_sp[0], 'является предком класса', requests_sp[1])
    elif requests_sp[1] not in cla_ss:  # ребенок не имеет ни одного родителя
        print('No', requests_sp[0], 'не является предком класса', requests_sp[1])
    # случай прямого наследования (родитель из запроса присутствует в списке родителей ребенка)
    elif requests_sp[1] in cla_ss and requests_sp[0] in cla_ss[requests_sp[1]]:
        print('Yes', requests_sp[0], 'является прямым предком класса', requests_sp[1])
    else:
        # запуск обработки запроса
        get_ans(cla_ss, requests_sp[0], requests_sp[1])
        if fl == 1:
            print('Yes', requests_sp[0], 'является предком класса', requests_sp[1])
        else:
            print('No', requests_sp[0], 'не является предком класса', requests_sp[1])