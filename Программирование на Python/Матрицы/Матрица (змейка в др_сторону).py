n = int(input())

n1 = 0              # 'номер спирали'
a = []
for i in range(n):  # 'Создание пустой матрицы размера n*n'
    a.append([0] * n)
d = 1
for k in range(n // 2):
    for i in range(n1, n - 1 - n1):  # 'Столбец вниз'
        a[i][n1] = d
        d = d + 1
    # '1 цикл закончен'
    for j in range(n1, n - 1 - n1):  # 'Строка вправо'
        a[n - 1 - n1][j] = d
        d = d + 1
    # '2 цикл закончен'
    for i in range(n - 1 - n1, n1, -1):  # 'Столбец вверх'
        a[i][n - 1 - n1] = d
        d = d + 1
    # '3 цикл закончен'
    for j in range(n - 1 - n1, n1, -1):  # 'Строка влево'
        a[n1][j] = d
        d = d + 1
    # '4 цикл закончен'

    n1 = n1 + 1                          # Делаем колечко меньше'

if n % 2 != 0:  # 'Проверка матрицы на четность/нечетность'
    a[n1][n1] = n * n

for i in range(0, n):                     # 'Печать матрицы'
    for j in range(0, n):
        print("{:>4}".format(a[i][j]), end=" ")
    print()
