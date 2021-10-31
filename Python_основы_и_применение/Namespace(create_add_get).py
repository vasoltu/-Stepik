# 'Создаем пустые словари'
# 'словарь для пространств: ключ - namespace; значение - parent'
name_space = {'global': None}
# 'словарь для объявленных переменных: ключ - namespace; значение - список переменных'
variables = {'global': []}


# создание словаря name_space
def create(namespace, parent):
    name_space.update({namespace: parent})
    # занесем  в словарь variables пространство namespace с пустым списком переменных
    add(namespace, [])


# создание словаря variables
def add(namespace, var):
    # пространство есть в словаре variables - добавь переменную в список
    if namespace in variables:
        variables[namespace] += [var]
    else:
        # создай новый ключ namespace и внеси переменную
        variables.update({namespace: [var]})


# 'поиск родителя для пространства namespace'
parent = ''
def find_parent(namespace):
    if namespace in name_space:
        parent = name_space[namespace]
        return parent
    else:
        return None


# 'поиск пространства, из которого объявлена переменная'
def get(namespace, var):
    if namespace not in name_space and namespace != 'global':
        return None
    elif namespace in variables and var in variables[namespace]:
        return namespace
    parent = find_parent(namespace)
    return get(parent, var)


n = int(input())
for j in range(n):
    task, namespace, variable = (str(i) for i in input().split())
    if task == 'create':
        create(namespace, variable)
    elif task == 'add':
        add(namespace, variable)
    elif task == 'get':
        print(get(namespace, variable))
