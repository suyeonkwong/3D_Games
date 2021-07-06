import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from day07.mydao import DaoStock
ds = DaoStock()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#X = [0, 0 ,0,0,0,0]
#Y = [0, 2 ,4,6,8,10]
Z = []

cal = DaoStock()
ds = cal.get_name()

for idx,i in enumerate(ds):
    X = [idx,idx,idx,idx,idx,idx]
    Y = [0,2,4,6,8,10]
    price = cal.get_prices(i)
    Z = price
    #print(Z)
    ax.plot(X, Y, Z)
plt.show()
