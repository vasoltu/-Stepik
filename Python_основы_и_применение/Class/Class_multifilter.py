
class Multi_filter:
    # решающие функции:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False
        # допускает элемент, если его допускают все функции (neg == 0)

    # конструктор класса, присваивает начальные значения
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.index = 0
        self.pos = 0
        self.neg = 0
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        return self
        # возвращает итератор по результирующей последовательности

    def __next__(self):
        self.pos = 0  # при каждой проверке нового числа из iterable обнуляем значения
        self.neg = 0
        if self.index < len(self.iterable):  # проходим по всему числам из диапазона iterable
            self.index = self.index + 1  # увеличиваем индекс
            for i in range(len(self.funcs)):  # проход по внешним функциям из *funcs
                if self.funcs[i](self.iterable[self.index - 1]):  # увеличиваем pos (true) или neg (false)
                    self.pos = self.pos + 1
                else:
                    self.neg = self.neg + 1
            if self.judge(self.pos, self.neg):  # применяем соответств. решающую функцию judge c полученным кол-вом pos и neg
                return self.iterable[self.index - 1]  # возвр. допущенный элемент последовательности iterable по его индексу
            else:
                return self.__next__()  # переход к следующему элементу пословательности iterable
        raise StopIteration  # исключение, которое останавливает итерацию по index

# допускаюшие функции
def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


# задание проверяемой последовательности из натуральных чисел от 0 до 30
a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(Multi_filter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(Multi_filter(a, mul2, mul3, mul5, judge=Multi_filter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(Multi_filter(a, mul2, mul3, mul5, judge=Multi_filter.judge_all)))
# [0, 30]
