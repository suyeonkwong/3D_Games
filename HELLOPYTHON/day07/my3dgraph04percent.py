import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock
import numpy as np

ds = DaoStock()
list_names = ds.get_name()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for idx,name in enumerate(list_names):
    
    x = np.zeros((6))+idx
    y = range(6)
    z = ds.get_prices(name)
    z_n = np.array(z)
    print(z_n)
    if z_n[0] == 0:
        continue
    z_n = z_n / z_n[0]
    ax.plot(x, y, z_n)
    
plt.show()
