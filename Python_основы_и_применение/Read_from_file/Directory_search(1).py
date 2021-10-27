import os

print(os.getcwd())
sp_dr = []

file = open('Test(d.s.)(вых.дн.).txt', 'w+')
for root, dirs, files in os.walk('main'):
    for _file in files:
        if _file[-3:] == '.py' and root not in sp_dr:
            print(root, file=file)
            sp_dr.append(root)
print(sp_dr)
file.close()


