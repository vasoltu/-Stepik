file = 'Test(п.с.)(вх.дн.).txt'
s = ''
for line in open(file, 'r'):  # 'Построчное чтение и склеивание в 1 строку'
    s = s + ' ' + line.rstrip()
sp = s.split()
leg = len(sp)
k = 0
print(sp)
file = open('Test(п.с.)(вых.дн.).txt', 'w+')
for i in range(leg):
    k += 1
    print(k, sp[-(i+1)])
    print(sp[-(i+1)], file=file)  # 'Запись инф. в файл'
file.close()
