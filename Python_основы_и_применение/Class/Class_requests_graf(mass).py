# ввод исходных ланных. Создание словаря
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


# сбор в один список всех родмтелей (прародмтелей) для child из запроса
def create_list(m_dict, parent, child):
    global list_of_parent
    if m_dict[child] == 'None':  # дошли до родителя, у которого нет прародителя, конец рекурсии
        return
    else:
        list_of_parent = list_of_parent + m_dict[child]  # поподнить список родителями очередного ребенка
        for element_of_child in m_dict[child]:  # бежит по списку родителей для очередного ребенка
            if element_of_child not in cla_ss:  # если у родмтеля не праводителя, пропусти
                continue
            else:
                # если прародитель есть, запусти рекурсию, взяв в качестве child его очередного родителя
                create_list(m_dict, parent, element_of_child)


# Основная программа
# объявление переменных
cla_ss = {}  # словарь для хранения данных о наследовании
requests = []  # хранит родмтеля и ребенка из очередного запроса
list_of_parent = []  # хранит список всех родмтелей (прародмтелей) для child из очередного запроса

# ввод исходных данных
n = int(input())  # к-во строк, описывающих наследование классов
for i in range(n):
    stroka1 = input()
    create_dict(cla_ss, stroka1)  # занесение данных в словарь из очередной строки

k = int(input())  # к-во запросов
for j in range(k):
    list_of_parent.clear()  # очистим список перед очередным использованием
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
        # создаем список всех родмтелей (прародмтелей) для child из запроса
        create_list(cla_ss, requests_sp[0], requests_sp[1])
        if requests_sp[0] in list_of_parent:
            print('Yes', requests_sp[0], 'является предком класса', requests_sp[1])
        else:
            print('No', requests_sp[0], 'не является предком класса', requests_sp[1])