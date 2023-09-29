import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dan1 =list(pd.read_csv('iris_data.csv')['Species'])
fib = plt.figure(figsize=(9,16))
ax1 = plt.add_subplot(211)
ax2 = plt.add_subplot(212)

b=0
n=0
b1=0
for i in range(len[dan1]):
    b = dan1.count(dan1[i])
    if b == b1:
        n = b
        N = dan1[i]
    elif b != n and b!=b1:
        a = b

    b1 = b
ax1 = plt.pie()