n = int(input())

n1 = 0              # 'номер спирали'
Matrix = []
for i in range(n):  # 'Создание пустой матрицы размера n*n'
    Matrix.append([0] * n)
unit = 1
for k in range(n // 2):
    for i in range(n1, n - 1 - n1):  # 'Столбец вниз'
        Matrix[i][n1] = unit
        unit = unit + 1
    # '1 цикл закончен'
    for j in range(n1, n - 1 - n1):  # 'Строка вправо'
        Matrix[n - 1 - n1][j] = unit
        unit = unit + 1
    # '2 цикл закончен'
    for i in range(n - 1 - n1, n1, -1):  # 'Столбец вверх'
        Matrix[i][n - 1 - n1] = unit
        unit = unit + 1
    # '3 цикл закончен'
    for j in range(n - 1 - n1, n1, -1):  # 'Строка влево'
        Matrix[n1][j] = unit
        unit = unit + 1
    # '4 цикл закончен'

    n1 = n1 + 1                          # Делаем колечко меньше'

if n % 2 != 0:  # 'Проверка матрицы на четность/нечетность'
    Matrix[n1][n1] = n * n

for i in range(0, n):                     # 'Печать матрицы'
    for j in range(0, n):
        print("{:>4}".format(Matrix[i][j]), end=" ")    # 'Форматированый вывод'
    print()
