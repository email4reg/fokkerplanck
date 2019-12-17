'''
Integrates with Euler method the Michaelis Menten model

If double comments ## are removed, numerically demonstrate the equivalence 
between one model with initial conditions on A and B states
and two models with initial conditions one on A and the second on B
'''

# Import libraries
import matplotlib.pyplot as plt

# Parameters
'''
NATIVE kc >> ko
EX1    ki >> kc 
EX2    ki << kc
'''
ko  = 0.01
kc  = 1
ki = 100

a0 = 0.8
b0 = 0.2
c0 = 0
t0 = 0
n = 100000
dt = 0.0001

# Set initial conditions
a = []; b =[]; c = []; t =[]
## a1 = []; b1 =[]; c1 = []
## a2 = []; b2 =[]; c2 = []
## c3 = []
a.append(a0); b.append(b0); c.append(c0); t.append(t0)
## a1.append(1); b1.append(0); c1.append(0)
## a2.append(0); b2.append(1); c2.append(0)
## c3.append(0)

# Integration
for i in range(1,n):
    t.append(t[i-1] + dt)    
    a.append(a[i-1] + dt*(-ko*a[i-1] + kc*b[i-1]))
    b.append(b[i-1] + dt*(ko*a[i-1]  - kc*b[i-1] - ki*b[i-1]))
    c.append(c[i-1] + dt*(ki*b[i-1]))
    ## a1.append(a1[i-1] + dt*(-ko*a1[i-1] + kc*b1[i-1]))
    ## b1.append(b1[i-1] + dt*(ko*a1[i-1]  - kc*b1[i-1] - ki*b1[i-1]))
    ## c1.append(c1[i-1] + dt*(ki*b1[i-1]))
    ## a2.append(a2[i-1] + dt*(-ko*a2[i-1] + kc*b2[i-1]))
    ## b2.append(b2[i-1] + dt*(ko*a2[i-1]  - kc*b2[i-1] - ki*b2[i-1]))
    ## c2.append(c2[i-1] + dt*(ki*b2[i-1]))
    ## c3.append(0.8*(c1[i-1] + dt*(ki*b1[i-1])) + 0.2*(c2[i-1]+dt*(ki*b2[i-1])))


# Plot
plt.figure(figsize=(8,6))
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')

plt.plot(t,c,color='black')
## plt.plot(t,c3,'--',color='red')

plt.xscale('log')
plt.xlabel('Time',fontsize=15)
plt.ylabel('D(t)',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)	
plt.show()

# %%