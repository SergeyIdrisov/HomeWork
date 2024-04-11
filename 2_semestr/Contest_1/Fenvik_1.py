
MAX = 1000001
Fenwick = [0] * MAX

def Summma0_i(i):
    result = 0
    while i >= 0:
        result += Fenwick[i]
        i = (i & (i + 1)) - 1
    return result

def IncElement(i, delta):
    while i < MAX:
        Fenwick[i] += delta
        i = (i | (i+1))

tests = int(input())
for _ in range(tests):
    n = int(input())
    Fenwick = [0] * MAX
    sum = 0
    estr = list(map(int, input().split()))
    for _ in estr:
        value = _
        IncElement(value, value)
        sum += Summma0_i(value-1)
    print(sum)