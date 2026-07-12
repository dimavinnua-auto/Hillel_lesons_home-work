print("first iterator")
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.lst[self.index]
        self.index -= 1
        return value


my_list = [20, 60, 350, 405, 505]
rev_iter = ReverseIterator(my_list)

for item in rev_iter:
    print(item)

print("second iterator")

class EvenIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


even_iter = EvenIterator(8)
for num in even_iter:
    print(num)