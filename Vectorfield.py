#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# %%
x = np.arange(-5,5,0.5)
y = np.arange(-5,5,0.5)

X, Y = np.meshgrid(x,y)

dy = -0.00001*X**3+ 0.0051*X**2-0.05*X
dx = np.ones(dy.shape)

plt.quiver(X,Y,dx,dy, color = 'purple')
plt.show()
# %%
a = 0.00001
b = 0.0051
c = 0.05

def f(x):
	y = (-1/4)*(a*x**4) + (1/3)*(b*x**3) - (1/2)*(c*x**2)
	return y

def derf(x):
	y = -(a*x**3) + (b*x**2) - (c*x)
	return y

def derderf(x):
	y = -3*a*x**2 + 2*b*x -c
	return y

x = np.linspace(0,1000)

plt.plot(x,f(x))
plt.title("Løsningskurve for N(t) ")
plt.xlabel("t")
plt.ylabel("N(t)")
#plt.xlim(0,50)
plt.ylim(0,60000)
plt.grid()
plt.legend()
plt.show()

# %%
plt.plot(x,derf(x))
plt.title("Hældningskurve for N'(t)")
plt.xlabel("t")
plt.ylabel("N'(t)")
#plt.xlim(0,50)
plt.ylim(-200,200)
plt.grid()
plt.show()
# %%
print(f'Der er {f(45.816)} bjørne efter 45.816 år og væksthastigheden vil være {derf(45.816)}')

# %%
