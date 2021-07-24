import sys    # 'Подключение библиотеки sys'
# 'Программа предназначена для запуска из консоли'
for i in sys.argv:
    if i == sys.argv[0]:
        continue
    else:
        print(i, end=' ')
