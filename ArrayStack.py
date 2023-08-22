import numpy as np

class ArrayStack:
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)

    def resize(self):
        b = self.new_array(max(1,2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i : int) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.a[i]

    def set(self, i : int, x : np.object) -> np.object:
        if i < 0 or i >= self.n:
            raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()
        for j in range(self.n - i, 0, -1):
            self.a[j] = self.a[j-1]
        self.a[i] = x
        self.n = self.n + 1


    def remove(self, i):
        if i < 0 or i > self.n:
            raise IndexError()
        x = self.a[i]
        for j in range(i, self.n - 2, -1):
            self.a[j] = self.a[j+1]
        self.n = self.n - 1
        if len(self.a) >= (3 * self.n):
            self.resize()
        return x

    def push(self, x):
        return self.add(self.n, x)

    def pop(self):
        return self.remove(self.n-1)

def test_Stack():
    s = ArrayStack()
    for i in range(5,0,-1):
        s.push(i)
    print("Initial array:\t", s.a)
    new = s.new_array(s.n)
    for i in range(5):
        new[i] = s.pop()
    print("array after removing:\t", new)


