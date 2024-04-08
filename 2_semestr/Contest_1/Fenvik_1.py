from copy import copy


class Fenvik(object):

    def __init__(self, n):
        if isinstance(n, int):
            self.n = n
            self.a = [0] * n
            return

        self.a = copy(n)
        self.n = len(self.a)
        for i in range(1, self.n + 1):
            j = i + (i & -i)  # parent in update tree
            if j <= self.n:
                self.a[j - 1] += self.a[i - 1]

    def __len__(self):
        return self.n

    def prefix_sum(self, i):
        #сумма от 0 до i-1
        assert 0 < i <= self.n
        res = 0
        while i > 0:
            res += self.a[i - 1]
            i &= i - 1
        return res

    def range_sum(self, i, j):
        #сумма от i до j-1
        assert 0 <= i <= j <= self.n
        res = 0
        while j > i:
            res += self.a[j - 1]
            j &= j - 1  # j -= j & -j
        while i > j:
            res -= self.a[i - 1]
            i &= i - 1
        return res

    def __getitem__(self, i):
        return self.range_sum(i, i + 1)

    def values(self):
        #Возвращает список всех значений
        res = copy(self.a)
        for i in range(self.n):
            res[i] = 0
        for i in range(1, self.n + 1):
            res[i - 1] += self.a[i - 1]
            j = i + (i & -i)
            if j <= self.n:
                res[j - 1] -= self.a[i - 1]
        return res

    def add(self, i, k):
        assert 0 <= i < self.n
        i += 1
        while i <= self.n:
            self.a[i - 1] += k
            i += i & -i

    def __setitem__(self, i, value):
        self.add(i, value - self[i])