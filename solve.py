import matplotlib.pyplot as plt

# NATIVE kc >> ko
# EX1    ki >> kc 
# EX2    ki << kc
ko  = 0.01
kc  = 1
ki = 100

a0 = 0.8
b0 = 0.2
c0 = 0
t0 = 0
n = 100000
dt = 0.0001

a = []; b =[]; c = []; t =[]
a.append(a0); b.append(b0); c.append(c0); t.append(t0)

for i in range(1,n):
    t.append(t[i-1] + dt)    
    a.append(a[i-1] + dt*(-ko*a[i-1] + kc*b[i-1]))
    b.append(b[i-1] + dt*(ko*a[i-1]  - kc*b[i-1] - ki*b[i-1]))
    c.append(c[i-1] + dt*(ki*b[i-1]))

plt.figure(figsize=(8,6))
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')

plt.plot(t,c,color='black')

plt.xscale('log')
plt.xlabel('Time',fontsize=15)
plt.ylabel('D(t)',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)	
plt.show()

# %%