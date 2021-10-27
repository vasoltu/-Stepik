import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, p_object):
        super(LoggableList, self).append(p_object)          # 'Добавление элемента в список'
        self.log(p_object)                                  # 'Вывод собщения'


z = LoggableList()
z.append('Hello!')
z.append('Good bye!')
print(z)