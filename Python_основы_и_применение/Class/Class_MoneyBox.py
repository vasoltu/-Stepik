# 'Вириртуальное хранилище денег '
class MoneyBox:
    # конструктор с аргументом – вместимость копилки
    def __init__(self, capacity):
        self.ca_pa = capacity

    # True, если можно добавить v монет, False иначе
    def can_add(self, v):
        if v <= self.ca_pa:
            return True
        elif v >= self.ca_pa:
            return False

    # положить v монет в копилку
    def add(self, v):
        self.ca_pa = self.ca_pa - v


# создали объект класса MoneyBox с начальным значением 10
x = MoneyBox(10)
print('Начальная вместимость копилки - ',x.ca_pa,'монет')
while x.ca_pa > 0:
   print('Сколько монет добавить?')
   v = int(input())
   rezult_can_add = x.can_add(v)
   if rezult_can_add == True:
        x.add(v)
        if x.ca_pa > 0:
            print('В копилку добавили',v, 'монет.','Осталось места для',x.ca_pa, 'монет')
        else:
            print('В копилку добавили', v, 'монет. Копилка полностью заполнена')
   else:
        print('В копилке нет места для', v, 'монет')

