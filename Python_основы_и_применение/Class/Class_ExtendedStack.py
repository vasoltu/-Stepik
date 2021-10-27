class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
        # операция сложения

    def sub(self):
        self.append(self.pop() - self.pop())
        # операция вычитания

    def mul(self):
        self.append(self.pop() * self.pop())
        # операция умножения

    def div(self):
        self.append(self.pop() // self.pop())
        # операция целочисленного деления


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    print(ex_stack.div())
    print(1, ex_stack.pop() == 2)
    print(ex_stack.sub())
    print(2, ex_stack.pop() == 6)
    print(ex_stack.sum())
    print(3, ex_stack.pop() == 7)
    print(ex_stack.mul())
    print(4, ex_stack.pop() == 2)
    print(len(ex_stack))


print(test())
