class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError()


z = PositiveList()
z.append(1)
z.append(-1)
print(z)
