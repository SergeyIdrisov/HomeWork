import matplotlib.pyplot as plt


def a_b(x, y):
    Ex = 0
    Ey = 0
    Exy = 0
    Ex2 = 0
    sum = len(x)
    A = 0
    for i in range(sum):
        Ex += x[i]
        Ey += y[i]
        Exy += x[i] * y[i]
        Ex2 += x[i] ** 2
    a = (Ex * Ey - sum * Exy) / (Ex ** 2 - sum * Ex2)
    b = (Ex * Exy - Ex2 * Ey) / (Ex ** 2 - sum * Ex2)
    for i in range(sum):
        y_sr = a * x[i] + b
        A += abs((y[i] - y_sr) / y[i])
    e = (A / sum) * 100
    y_sr = Ey/sum
    x_sr = Ex/sum
    return a, b, e, y_sr, x_sr
n = int(input())
y = [list(map(int, input().split()))for i in range(n)]
x = [list(map(int, input().split()))for i in range(n)]
fib = plt.figure(figsize=(16,9))
ax1 = fib.add_subplot()
for i in range(n):
    a,b,e, y_sr, x_sr = a_b(x[i], y[i])
    print(a,b,e)
    ax1.errorbar (x[i],y[i], yerr = e*y_sr/100, xerr = e*x_sr/100, color = 'k', linestyle = 'None', marker = 'o')
    pot = []
    for j in range(len(x[i])):
        v = a*x[i][j] + b
        pot.append(v)
    ax1.plot(x[i], pot, 'r')
plt.xlabel('$N^{o}$')
plt.ylabel('$L_{k}-L_{1}$, mm')
plt.legend()
plt.show()