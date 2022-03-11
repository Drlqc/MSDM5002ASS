# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:13:44 2021

@author: 10239
"""
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

import numpy as np


ax = plt.axes(projection='3d',proj_type='ortho')



x1 = np.linspace(0,1,6)
y1  =z1 = np.array([0 for i in range(6) ])

x2 = z2 = y1
y2 = x1

x3 = y3 = y1
z3 = x1

x4 = np.array([0 for i in range(6) ])
y4 = np.linspace(0,1,6)
z4 = np.array([1 for i in range(6) ])

x5 =x4
y5 = z4
z5 = y4

x6 = np.linspace(0,1,6)
y6 = np.array([0 for i in range(6) ])
z6 = np.array([1 for i in range(6) ])

x7 = z6
y7 = np.array([0 for i in range(6) ])
z7 = np.linspace(0,1,6)

x8 = np.linspace(0,1,6)
y8 = np.array([1 for i in range(6) ])
z8 = np.array([0 for i in range(6) ])

x9 = np.linspace(0,1,6)
y9 = np.array([1 for i in range(6) ])
z9 = np.array([1 for i in range(6) ])

x10 =  np.array([1 for i in range(6) ])
y10 = np.linspace(0,1,6)
z10 = np.array([0 for i in range(6) ])

x11 =  np.array([1 for i in range(6) ])
y11 = np.linspace(0,1,6)
z11 = np.array([1 for i in range(6) ])

z12 = np.linspace(0,1,6)
x12  =y12 = np.array([1 for i in range(6) ])

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.ylim(0,1)
plt.xticks([0,0.2,0.4,0.6,0.8,1])
plt.yticks([0,0.2,0.4,0.6,0.8,1])
# plt.zticks([0,0.2,0.4,0.6,0.8,1])
for i in range(len(x1)):
    if i ==5:
        ax.scatter(x1[i],y1[i],z1[i],c='r',marker='*')


        plt.savefig(str(i)+'.png')
        plt.pause(0.5)
        break

        
    ax.scatter(x1[i],y1[i],z1[i],c='r',marker='*')


    plt.savefig(str(i)+'.png')
    plt.pause(0.5)


for i in range(len(x1)):

    ax.scatter(x2[i],y2[i],z2[i],c='r',marker='*')

    plt.savefig(str(i+6*1)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):

    
    ax.scatter(x3[i],y3[i],z3[i],c='r',marker='*')

    plt.savefig(str(i+6*2)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):

    ax.scatter(x4[i],y4[i],z4[i],c='r',marker='*')

    plt.savefig(str(i+6*3)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x5[i],y5[i],z5[i],c='r',marker='*')

    plt.savefig(str(i+6*4)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x6[i],y6[i],z6[i],c='r',marker='*')

    plt.savefig(str(i+6*5)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x7[i],y7[i],z7[i],c='r',marker='*')

    plt.savefig(str(i+6*6)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x8[i],y8[i],z8[i],c='r',marker='*')

    plt.savefig(str(i+6*7)+'.png')
    plt.pause(0.5)


for i in range(len(x1)):
    ax.scatter(x9[i],y9[i],z9[i],c='r',marker='*')

    plt.savefig(str(i+6*8)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x10[i],y10[i],z10[i],c='r',marker='*')
    

    plt.savefig(str(i+6*9)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x11[i],y11[i],z11[i],c='r',marker='*')

    plt.savefig(str(i+6*10)+'.png')
    plt.pause(0.5)

for i in range(len(x1)):
    ax.scatter(x12[i],y12[i],z12[i],c='r',marker='*')

    plt.savefig(str(i+6*11)+'.png')
    plt.pause(0.5)




# ax.plot(const1+center_cube[0], line+center_cube[1], height1+center_cube[2], zdir='z',c='b')
# ax.plot(const2+center_cube[0], line+center_cube[1], height1+center_cube[2], zdir='z',c='b')
# ax.plot(line+center_cube[0], const1+center_cube[1], height1+center_cube[2], zdir='z',c='b')
# ax.plot(line+center_cube[0], const2+center_cube[1], height1+center_cube[2], zdir='z',c='b')

# ax.plot(const1+center_cube[0], line+center_cube[1], height2+center_cube[2], zdir='z',c='b')
# ax.plot(const2+center_cube[0], line+center_cube[1], height2+center_cube[2], zdir='z',c='b')
# ax.plot(line+center_cube[0], const1+center_cube[1], height2+center_cube[2], zdir='z',c='b')
# ax.plot(line+center_cube[0], const2+center_cube[1], height2+center_cube[2], zdir='z',c='b')

# ax.plot(const1+center_cube[1], line+center_cube[2], height2+center_cube[0], zdir='x',c='b')
# ax.plot(const2+center_cube[1], line+center_cube[2], height2+center_cube[0], zdir='x',c='b')
# ax.plot(const1+center_cube[1], line+center_cube[2], height1+center_cube[0], zdir='x',c='b')
# ax.plot(const2+center_cube[1], line+center_cube[2], height1+center_cube[0], zdir='x',c='b')



# plt.axis('square')

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# theta=45
# alpha=50







# num_points=40
# radius=10
# alpha=np.linspace(0,np.pi*2,num_points,endpoint=True)
# x=np.zeros(num_points,float)
# y=np.zeros(num_points,float)
# for ni in range(num_points):
#     x[ni]=radius*np.cos(alpha[ni])
#     y[ni]=radius*np.sin(alpha[ni])

# plt.figure()
# plt.axis('square')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim([int(min(x)-1.1), int(max(x)+1.1)])
# plt.ylim([int(min(y)-1.1), int(max(y)+1.1)])

# # plt.plot(x,y,'r.')

# x_num=len(x)
# for ni in range(x_num):
#     plt.title(['step=', ni],color='blue',fontsize=20)    
#     plt.plot(x[ni],y[ni],'-ro',markersize=5)
#     plt.savefig(str(ni)+'.png')
#     plt.pause(0.5)