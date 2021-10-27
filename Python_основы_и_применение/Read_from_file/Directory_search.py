import os

print(os.getcwd())
sp_dr = []
sp_dr_cl = []

for root, dirs, files in os.walk('main'):
    for _file in files:
        if _file[-3:] == '.py':
            sp_dr.append(root)

file = open('Test(d.s.)(вых.дн.).txt', 'w+')
for i in range(len(sp_dr)):
    if sp_dr[i] not in sp_dr_cl:
        print(sp_dr[i], file=file)
        sp_dr_cl.append(sp_dr[i])
print(sp_dr_cl)
file.close()
