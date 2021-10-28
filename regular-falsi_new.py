import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Cox(x) - 1.3x = 0
def f(x):
 return np.cos(x) - 1.3*x
 
 def regular_falsi(a, b, tol):
 iter_list = []
 a_list = []
 b_list = []
 c_list = []

 count = 0
 MAX_ITER = 20

 for i in range(MAX_ITER):
 c = ( a * f(b) - b * f(a) ) / ( f(b) - f(a) )
 count += 1

 if ( np.abs(f(c)) ) < tol:
 break

 if f(c) * f(a) < 0:
 b = c
 else:
 a = c

 iter_list.append(count)
 a_list.append(a)
 b_list.append(b)
 c_list.append(c)

 return c, count, a_list, b_list, c_list, iter_list
 
 a = -2
b = 2
tol = 0.0001
root, count, a_list, b_list, c_list, iter_list = regular_falsi(a, b, tol)

print('Root is: ',root)
print('Iterations performed: ',count)

Regularfalsivalues = {
 'Iterations ': iter_list,
 'a ' : a_list,
 'b ' : b_list,
 'Root ': c_list
}
df = pd.DataFrame(Regularfalsivalues)
df

plt.title('REGULAR FALSI METHOD')
plt.grid()
x = np.linspace(-5,5)
y = f(x)
plt.scatter(root,f(root),color = 'r')
plt.plot(x,y)
plt.show()
