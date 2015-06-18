__author__ = 'lenz'
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.integrate as it

dt=0.1e-6
dz=1
eps0=8.854e-12
mu0=4*(math.pi)*1e-7
H=4e3 #meters
D=2e3 #meters
v=8e7 #m/s
c=1/math.sqrt(mu0*eps0) #m/s
R=math.sqrt(H**2+D**2)
theta=math.asin(D/R) #rad
theta_deg=theta*180/math.pi #degrees

t=np.arange(0,25e-6,dt)
a=np.matrix.transpose(t)

I=np.zeros(len(t))
index=1e-6/dt
I[0:index+1]=(10e3/1e-6)*t[0:index+1]
I[index+1:-1]=-(10e3/24e-6)*t[index+1:-1]+(10e3+10e3/24)
print(len(I))
print(H/v)
Iz=np.zeros((int(H/dz),len(t) + int(H/v/dt)))

for i in range(0,int(H/dz)): #height
    print(int(i*dz/v/dt))

#     Iz[i,int(i*dz/v/dt)]=I

#     #for j in range(0,len(t)): #time
#         Iz[i,int(i*dz/v/dt)]=I


plt.plot(t,I)
plt.show()
# print(H/v)
# Ez=(1/(2*(math.pi)*eps0))*[lambda z,t: ((2-3*((np.sin(theta))**2))/(R**3))*I, 0, H, ]
    # it.dblquad(lambda z,  (2-3*np.(sin(theta)**2))/(R**3))]
