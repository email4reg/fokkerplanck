import numpy as np

# NATIVE kc >> ko
# EX1    ki >> kc 
# EX2    ki << kc
#ko  = 1e-6
ki = 1e-3
kc  = np.logspace(-3,3,1000)*ki

def init_b(ko,kc,ki):
    delta = np.sqrt((ko+kc+ki)**2 - 4*ki*ko)
    a2 = (ko+kc+ki - delta - (2*ki*ko)/(ki+ko)) / (2*delta)
    a3 = - (ko+kc+ki + delta - (2*ki*ko)/(ki+ko)) / (2*delta)
    u2 = - (kc+ki+ko + delta) / (2*ki)
    u3 = - (kc+ki+ko - delta) / (2*ki)
    b_0 = a2*u2 + a3*u3
    return b_0

b0 = []
for kc_v in kc:
    ko = kc_v/ki*1e-3
    b0.append(init_b(ko,kc_v,ki))

plt.figure(figsize=(8,6))
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
    
plt.plot(kc,b0,color='black',label='ko/kc = 1E-3 (NATIVE)')

plt.text(1e-6,0.15,'EX2 limit',fontsize=20)
plt.text(5e-2,0.85,'EX1 limit',fontsize=20)

plt.xscale('log')
plt.xlabel('kc/ki',fontsize=15)
plt.ylabel('B(0)',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)	
plt.legend(fontsize=15)
plt.show()


# %%