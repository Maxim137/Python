import numpy as np
import scipy.integrate
import math
import matplotlib.pyplot as plt

print('Enter a1')

a1 = float(input())

print('Enter a2<=a1')

while True:
	try:
		a2 = float(input())
		if a2 > a1:
			raise Exception
		break
	except Exception:
		print('Enter a2<=a1')

print('Enter a3<=a2')

while True:
	try:
		a3 = float(input())
		if a3 > a2:
			raise Exception
		break
	except Exception:
		print('Enter a3<=a2')

print('Enter number of steps')
N = int(input())

print('Enter x_min >= a1')

while True:
	try:
		x_min = float(input())
		if x_min < a1:
			raise Exception
		break
	except Exception:
		print('Enter x_min >= a1')

print('Enter x_max > x_min')

while True:
	try:
		x_max = float(input())
		if x_max <= x_min:
			raise Exception
		break
	except Exception:
		print('Enter x_max > x_min')

print('Enter y_min >= a2')

while True:
	try:
		y_min = float(input())
		if y_min < a2:
			raise Exception
		break
	except Exception:
		print('Enter y_min >= a2')

print('Enter y_max > y_min')

while True:
	try:
		y_max = float(input())
		if y_max <= y_min:
			raise Exception
		break
	except Exception:
		print('Enter y_max > y_min')

x1 = np.zeros(N)
x2 = np.zeros(N)
potential = np.zeros((N, N))

for i in range (N):
	x1[i] = x_min + (x_max-x_min)*i/(N-1)
	x2[i] = y_min + (y_max-y_min)*i/(N-1)

for i in range (N):

	for j in range (N):
		lam = ( -(a1**2+a2**2)+math.sqrt((a1**2+a2**2-x1[i]**2-x2[j]**2)**2 - 4*(a1**2*a2**2-x1[i]**2*a2**2-x2[j]**2*a1**2)) ) / 2
		#print (lam)
		f = lambda v: (1 - x1[i]**2/(a1**2+v) - x2[j]**2/(a2**2+v) ) / math.sqrt((a1**2+v)*(a2**2+v)*(a3**2+v))
		integral = scipy.integrate.quad(f,lam,np.inf)[0]
		potential[i, j] = 3/4*math.sqrt(a1**2-a3**2)*integral
		#print(integral)

print(potential)

xval = np.linspace(x_min, x_max, N)
yval = np.linspace(y_min, y_max, N)
x, y = np.meshgrid(xval, yval)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, potential, cmap = 'plasma')
plt.show()