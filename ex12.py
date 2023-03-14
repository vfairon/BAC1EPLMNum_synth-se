import numpy as np
from math import cos,sin,pi
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline as spline
from matplotlib import cm

X = np.array([-1,-1,1,1])
Y = np.array([-1,1,1,-1])

T = np.array([28,2,40,37])
x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

phi_1 = np.zeros((len(x),len(y)))
phi_2 = np.zeros((len(x),len(y)))
phi_3 = np.zeros((len(x),len(y)))
phi_4 = np.zeros((len(x),len(y)))

for i_x in range(len(x)):
    for i_y in range(len(y)):
        phi_1[i_x,i_y] = ((y[i_y]-1)*(x[i_x]-1))/4
        phi_2[i_x,i_y] = (-(y[i_y]+1)*(x[i_x]-1))/4
        phi_3[i_x,i_y] = ((y[i_y]+1)*(x[i_x]+1))/4
        phi_4[i_x,i_y] = (-(y[i_y]-1)*(x[i_x]+1))/4



phis = np.transpose(np.concatenate(([phi_1],[phi_2],[phi_3],[phi_4]), axis = 0))
#print(phis)
z  = phis @ T
x_3, y_3 = np.meshgrid(x, y)




fig = plt.figure(figsize = (12,10))

ax = plt.axes(projection='3d')
ax.scatter(X,Y,T,color = 'red',s=100)
#surf1 = ax.plot_surface(x_3[25:50,25:50], y_3[25:50,25:50], phi_1[25:50,25:50], cmap = plt.cm.cividis)
#surf2 = ax.plot_surface(x_3[25:50,25:50], y_3[50:75,50:75], phi_2[25:50,50:75], cmap = plt.cm.cividis)
#surf3 = ax.plot_surface(x_3[50:75,50:75], y_3[50:75,50:75], phi_3[50:75,50:75], cmap = plt.cm.cividis)
#surf4 = ax.plot_surface(x_3[50:75,50:75], y_3[25:50,25:50], phi_4[50:75,25:50], cmap = plt.cm.cividis)
#surf1 = ax.plot_surface(x_3[25:75,25:75], y_3[25:75,25:75], z[25:75,25:75], cmap = plt.cm.cividis)
surf1 = ax.plot_surface(x_3, y_3, z, cmap = plt.cm.cividis)

# Set axes label#
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

fig.colorbar(surf1, shrink=0.5, aspect=8)


plt.show()