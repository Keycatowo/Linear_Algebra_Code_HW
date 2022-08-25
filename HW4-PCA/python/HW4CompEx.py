#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections
import os
#%% Random Generate data
N = 250
np.random.seed(1)
A = np.random.normal(size=[N,2])
B = np.array([[0.5, 0.5], [0.6, -0.1]])
X = np.matmul(A,B) # randomly create two correlated columns
#%% find a change of coordinates to diagonalize the covariance matrix.
mu = np.mean(X, axis=0)
X_new = X - np.tile(mu, [N,1])

#%% Finish this part 
# TODO: Use diagonalization to get the pinciple axes.
# Sigma = ... <-expected value of the covariance matrix
# Q = ... <-eigenvectors matrix, Q[:,0] is the first eigenvectors
# D = ... <-diagonal matrix with eigenvalues
# prinAxes = ... <-Reconstruct the pinciple axes
Sigma = 1/N * np.matmul(X_new.T, X_new); 
w, Q = np.linalg.eig(Sigma)
D = np.array([[w[0], 0], [0, w[1]]])
prinAxes = np.matmul(Q, np.sqrt(D))
#%% 
Y = np.matmul(X_new, Q) + np.tile(mu, [N,1])
plt.scatter(X[:,0], X[:,1], s=3, c="blue", marker="8")
plt.scatter(Y[:,0], Y[:,1], s=3, c="green", marker="v")
plt.plot([0,prinAxes[0,0]], [0, prinAxes[1,0]], linewidth=2, color="red")
plt.plot([0,prinAxes[0,1]], [0, prinAxes[1,1]], linewidth=2, color="red")
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.show()

#%% Total Error with Principle components
# When we project the points on different axes, 
# we will get different errors.
# This part will show you the total errors 
# when we project the points on the two principle components.

def get_error(x0, y0,m):
    """ Get Distance and Location with Line y=ax and Point (x0,y0)

        dis: The minimal distance bewteen (x0,y0) and y=ax.
        (x1, y1): The point in y=ax with minimal distance.
    """
    x1 = (y0*m + x0)/(m*m+1)
    y1 = x1*m
    dis = (x0 - x1)**2 + (y0 - y1)**2
    return dis, x1, y1 
``
m_axe1 = prinAxes[1,0] / prinAxes[0,0]
m_axe2 = prinAxes[1,1] / prinAxes[0,1]

# Get each distance of each point
x0s = X[:,0]
y0s = X[:,1]
# PC_1
ans = np.apply_along_axis(lambda P: get_error(x0=P[0], y0=P[1], m=m_axe1), axis=1, arr=X)
x1s,y1s,dis1 = ans[:,1], ans[:,2], ans[:,0]
lines1 = [[(x0, y0), (x1, y1)] for x0, y0, x1, y1 in zip(x0s, y0s, x1s, y1s)]
# PC_2
ans = np.apply_along_axis(lambda P: get_error(x0=P[0], y0=P[1], m=m_axe2), axis=1, arr=X)
x1s,y1s,dis2 = ans[:,1], ans[:,2], ans[:,0]
lines2 = [[(x0, y0), (x1, y1)] for x0, y0, x1, y1 in zip(x0s, y0s, x1s, y1s)]

# %%
fig,axes=plt.subplots(1,2)
for index, (lines, m, dis) in enumerate([(lines1, m_axe1, dis1), (lines2, m_axe2, dis2)]):
    segments = collections.LineCollection(lines, color="#2A9D8F", linewidth = 0.5)
    axes[index].add_collection(segments)
    axes[index].plot([-3, 3], [-3*m, 3*m], c="#E9C46A")
    axes[index].scatter(x0s, y0s, s=3, c="#E76F51")
    axes[index].set_aspect(1)
    axes[index].set_xlim([-2,2])
    axes[index].set_ylim([-2,2])
    axes[index].set_title(f"Total Error with PC_{index+1}: \n{sum(dis):.2f}")
plt.show()

# %% Total Error with arbitary axes
# This part will show you how the total Error change 
# when we change the axes.
# NOTE: If you feel the process is too slow, 
#       you can reduce the size N or num_degrees.
from pathlib import Path
Path("output").mkdir(exist_ok=True)
num_degrees = 180
thetas = np.deg2rad(np.linspace(0,360,num_degrees))
ms = np.tan(thetas) # m = y/x = tan(theta)
for index, m in enumerate(ms):
    fig, axes = plt.subplots()
    ans = np.apply_along_axis(lambda P: get_error(x0=P[0], y0=P[1], m=m), axis=1, arr=X)
    x1s,y1s,dis = ans[:,1], ans[:,2], ans[:,0]
    lines = [[(x0, y0), (x1, y1)] for x0, y0, x1, y1 in zip(x0s, y0s, x1s, y1s)]
    segments = collections.LineCollection(lines, color="#2A9D8F", linewidth = 0.5)
    axes.add_collection(segments)
    axes.plot([-3, 3], [-3*m, 3*m], c="#E9C46A")
    axes.scatter(x0s, y0s, s=3, c="#E76F51")
    axes.set_aspect(1)
    axes.set_xlim([-2,2])
    axes.set_ylim([-2,2])
    axes.set_title(f"Total Error:\n{sum(dis):.2f}")
    plt.savefig(f"output/{index}.png")
    plt.show()
# %%
# plot with gif animation
import imageio
from glob import glob
with imageio.get_writer("Error change.gif", mode="I") as writer:
    for i in range(num_degrees):
        filename = f"output/{i}.png"
        img = imageio.imread(filename)
        writer.append_data(img)

# %%
