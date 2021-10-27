class Buffer:
    def __init__(self):
        self.listing = []
        # конструктор без аргументов

    def add(self, *a):
        b = list(a)
        self.listing = self.listing + b
        length = len(self.listing)
        while True:
            # self.listing = self.listing + b
            if length >= 5:
                print(self.listing[0] + self.listing[1] + self.listing[2] + self.listing[3] + self.listing[4])
                for i in range(5):
                    self.listing.pop(0)
                length = len(self.listing)
            elif length < 5:
                break
        # добавить следующую часть последовательности

    def get_current_part(self):
        return self.listing
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены


buf = Buffer()
print(1, buf.add(1, 2, 3))
print(2, buf.get_current_part())  # вернуть [1, 2, 3]
print(3, buf.add(4, 5, 6))  # print(15) – вывод суммы первой пятерки элементов
print(4, buf.get_current_part())  # вернуть [6]
print(5, buf.add(7, 8, 9, 10))  # print(40) – вывод суммы второй пятерки элементов
print(6, buf.get_current_part())  # вернуть []
print(7, buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(8, buf.get_current_part())  # вернуть [1]
