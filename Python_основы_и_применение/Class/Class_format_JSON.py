import json

di = {}  # словарь наследования в paton
sp_child = []  # список детей
sp_child_sort = []  # список детей сортированный
count = 0

# определяет есть ли путь из start  в end, т.е. яв-ся ли start родителем end
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return 1
    if start not in graph:
        return 0
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path: return 1
    return 0


js = json.loads(input())  # ввод строки в json
# формируем словарь: ключ - child, значение - список parent
k = len(js)
for i in range(k):
    sp_child.append(js[i]['name'])
    di[js[i]['name']] = js[i]['parents']
sp_child_sort = sorted(sp_child)
for j in range(len(di)):
    for u in range(len(di)):
        r = find_path(di, sp_child_sort[u], sp_child_sort[j], path=[])
        if r == 1:
            count += 1
    print(sp_child_sort[j], ':', count)
    count = 0
