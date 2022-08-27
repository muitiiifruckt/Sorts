import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [66,66+5,66+10,66+15,66+19,66+24,66+34,66+38]
y = [23,20,17,11,9,7,4,2]
x1=[66,66+38]
y1=[23,2]
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(ticker.MultipleLocator(3))

ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))


ax.grid()
ax.grid(which='major',
        color = 'k')
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')
ax.set_xlabel('вес ( мой вес+ доп вес) (кг)')
ax.set_ylabel('количество повторений ()')
ax.scatter(x, y,
           c = 'deeppink')
plt.plot(x, y)
plt.plot(x1, y1)
plt.show()