import numpy as np
import matplotlib.pyplot as plt
t = np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47])
p = np.array([4.369447852, 4.33073334, 4.248495242, 4.110873864, 3.871201011, 3.828641396, 3.610917913, 3.433987204, 3.17805383, 3.135494216, 2.995732274, 2.890371758, 2.833213344, 2.772588722, 2.708050201, 2.63905733, 2.564949357, 2.564949357, 2.48490665, 2.48490665, 2.48490665, 2.48490665, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.397895273, 2.302585093, 2.302585093, 2.302585093, 2.302585093, 2.302585093, 2.302585093, 2.302585093, 2.302585093])
v = t
u = np.log(p)
k1, b1 = np.polyfit(v, u, 1)
mu = np.mean(u) # средее
mv = np.mean(v)
mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
N = len(v)
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ))
print(k1, b1)
print(sigma_k)
x = np.array([0. , 26])
fig, ax = plt.subplots()
ax.errorbar(v, u , yerr=sigma_k, fmt = '.', linestyle=None, label='Экспериментальные точки')
ax.plot(x, k1 * x + b1, label='Линейная аппроксимация')
ax.set_title('Рис.2. Зависимость ln(P-Pпр/P0) от t при улучшении вакуума(1)')
ax.set_ylabel('ln(P-Pпр)/Po)')
ax.set_xlabel('t, с')
ax.legend()
plt.show()
