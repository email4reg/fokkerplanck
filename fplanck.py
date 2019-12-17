"""
Integration of Fokker Planck equation
=========================================================
Method: finite difference with upward derivative scheme 
Note:   introduces dissipation
=========================================================
Parameters
  L       upper limit through which integration is performed
  n       number of nodes over which integration is performed 
          for binomial distribution n=L because only integer values can be assumed
  T1s     lower boundary condition
  T2s     upper boundary condition
  alpha   diffusion term of first population
  alpha2  diffusion term of second population
  mu      drift velocity of first population
  mu2     drift velocity of second population
  t_final final time: end of the simulation
  dt      integration time step
  size1   dimension of the first population
  size2   dimension of the second population
  =======================================================
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 20
n = L
T1s = 0; T2s = 0
dx = L/n

alpha = 1e-6;   alpha2 = 1e-6
mu = 0.08;       mu2 = 0.08

t_final = 120
dt = 0.1

size1 = 5
size2 = 1

# Drift and Diffusion terms
# Currently set to constant, can become function of space or time
def drift_fun(x,mu):
    return mu

def diff_fun(x,alpha):
    return alpha

# Setting grid
x = np.linspace(dx/2, L-dx/2, n)

# Initial conditions of first population
initial_points = np.random.binomial(1,0.,size=size1)    
hist_val = plt.hist(initial_points,bins=n,range=(0,L),density=True)
T = hist_val[0]

# Initial conditions of second population
initial_points2 = np.random.binomial(1,0.,size=size2)    
hist_val2 = plt.hist(initial_points2,bins=n,range=(0,L),density=True)
T2 = hist_val2[0]

# Initial conditions of total population
Ttot0 = (T + T2)/2
Ttot = (T + T2)/2

# Numerical integration
# using finite differences method with upward scheme
# plot is included
# two commented command lines are inserted; delete the comment to save figures every 200 steps
dTdt = np.empty(n)
dTdt2 = np.empty(n)
t = np.arange(0, t_final, dt)
for j in range(0,len(t)):
    plt.clf()
    for i in range(1,n-1):
        dTdt[i]  = -drift_fun(x[i],mu)*(T[i]-T[i-1])/dx + diff_fun(x[i],alpha)*(-(T[i]-T[i-1])/dx**2 + (T[i+1]-T[i])/dx**2)
        dTdt2[i] = -drift_fun(x[i],mu2)*(T2[i]-T2[i-1])/dx + diff_fun(x[i],alpha2)*(-(T2[i]-T2[i-1])/dx**2 + (T2[i+1]-T2[i])/dx**2)
    dTdt[0]    = -drift_fun(x[0],mu)*(T[0]-T1s)/dx + diff_fun(x[i],alpha)*(-(T[0]-T1s)/dx**2 + (T[1]-T[0])/dx**2)
    dTdt[n-1]  = -drift_fun(x[n-1],mu)*(T[n-1]-T[n-2])/dx + diff_fun(x[i],alpha)*(-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
    dTdt2[0]   = -drift_fun(x[0],mu2)*(T2[0]-T1s)/dx + diff_fun(x[i],alpha2)*(-(T2[0]-T1s)/dx**2 + (T2[1]-T2[0])/dx**2)
    dTdt2[n-1] = -drift_fun(x[n-1],mu2)*(T2[n-1]-T2[n-2])/dx + diff_fun(x[i],alpha2)*(-(T2[n-1]-T2[n-2])/dx**2 + (T2s-T2[n-1])/dx**2)
    T = T + dTdt*dt
    T2 = T2 + dTdt2*dt
    Ttot = (T + T2)/2
        
    plt.figure(1)
    plt.scatter(x,Ttot,color='black')
    for k in range(len(x)):
        plt.vlines(x[k],ymin=0,ymax=Ttot[k],color='black')
    time = str(round(dt*j+dt,1))
    prob = str(round(sum(Ttot),3))
    plt.title('Time = '+time+'               Prob = '+prob,fontsize=15)
    plt.xlabel('m/z',fontsize=15)
    plt.grid(linestyle=':')
    #if j%200 == 0:
    #   plt.savefig('pdf_1pop'+str(j)+'.png')

    plt.show()
    plt.pause(0.001)

# %%