import numpy as np
import scipy.integrate
import math
import matplotlib.pyplot as plt

print('Enter a1')
a1 = float(input())

print('Enter a2<=a1')
a2 = float(input())

while a2>a1:
	print('Enter a2<=a1')
	a2 = float(input())

print('Enter a3<=a2')
a3 = float(input())

while a3>a2:
	print('Enter a3<=a2')
	a3 = float(input())

print('Enter number of steps')
N = int(input())

print('Enter x_min >= a1')
x_min = float(input())

while x_min<a1:
	print('Enter x_min >= a1')
	x_min = float(input())

print('Enter x_max > x_min')
x_max = float(input())

while x_max<=x_min:
	print('Enter x_max > x_min')
	x_max = float(input())


print('Enter y_min >= a2')
y_min = float(input())

while y_min<a2:
	print('Enter y_min >= a2')
	y_min = float(input())

print('Enter y_max > y_min')
y_max = float(input())

while y_max<=y_min:
	print('Enter y_max > y_min')
	y_max = float(input())

x1 = np.linspace(x_min, x_max, N)
x2 = np.linspace(y_min, y_max, N)
x, y = np.meshgrid(x1, x2)

potential = np.zeros((N, N))

#print (x1)
#print (x2)

for i in range (N):

	for j in range (N):
		lam = ( math.sqrt( (a1**2 + a2**2 - x1[i]**2 - x2[j]**2)**2 - 4*(a1**2* a2**2 - x1[i]**2 * a2**2 - x2[j]**2 * a1**2) ) - (a1**2 + a2**2) ) / 2
		#print (lam)
		f = lambda v: (1 - (x1[i]**2 / (a1**2 + v)) - (x2[j]**2 / (a2**2 + v)) ) / math.sqrt((a1**2 + v) * (a2**2 + v) * (a3**2 + v))
		integral = scipy.integrate.quad(f, lam, np.inf)[0]
		potential[i, j] = 3/4*math.sqrt(a1**2 - a3**2)*integral
		#print(integral)

#print(potential)

fig = plt.figure()
graph = fig.add_subplot(xlabel='X', ylabel='Y',zlabel='Potential', projection='3d')
graph.plot_surface(x, y, potential	, cmap = 'jet')

plt.show()
