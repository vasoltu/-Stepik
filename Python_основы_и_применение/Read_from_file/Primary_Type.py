# import модуля csv для работа с форматом и из модуля collections import Counter для подсчета частых видов преступлений
import csv
from collections import Counter
a = []
# открытие файла
with open('Crimes.csv') as r:
    reader = csv.DictReader(r)
    # поциклавая запись искомого значения
    for cr in reader:
        a.append(cr['Primary Type'])

# подсчет частых видов преступлений
c = Counter(a).most_common(1)
print(c)
