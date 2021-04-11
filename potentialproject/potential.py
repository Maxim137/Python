
__enter__ = ('enter')
__check__ = ('check')
__grid__ = ('grid')
__integ__ = ('integ')
__plot__ = ('plot')
__main__ = ('main')

def enter():

	print('Enter a1')
	a1 = float(input())

	print('Enter a2<=a1')
	a2 = float(input())

	print('Enter a3<=a2')
	a3 = float(input())

	print('Enter x_min >= a1')
	x_min = float(input())

	print('Enter x_max > x_min')
	x_max = float(input())

	print('Enter y_min >= a2')
	y_min = float(input())

	print('Enter y_max > y_min')
	y_max = float(input())

	print('Enter number of steps')
	N = int(input())

	return a1, a2, a3, x_min, x_max, y_min, y_max, N

def check(q1, q2, q3, q4, q5, q6, q7):
	""" Проверка значений полуосей(a1>=a2>=a3) и границ рассчёта потенциала (x_max > x_min > a1, y_max > y_min > a2) """
	k = 0
	if q2>q1:
		#print('Enter a2 <= a1')
		k = 1
	if q3>q2:
		#print('Enter a3 <= a2')
		k = 1
	if q4<q1:
		#print('Enter x_min >= a1')
		k = 1
	if q5<=q4:
		#print('Enter x_max > x_min')
		k = 1
	if q6<q2:
		#print('Enter y_min >= a2')
		k = 1
	if q7<=q6:
		#print('Enter y_max > y_min')
		k = 1

	if k == 0:
		return True
	if k == 1:
		return False

def grid(x_min, x_max, y_min, y_max, N):
	""" Создание массива значений координат (x1, x2) для вычисления интеграла (potential) и сетки (x, y) для графика """
	import numpy as np

	x1 = np.linspace(x_min, x_max, N)
	x2 = np.linspace(y_min, y_max, N)
	x, y = np.meshgrid(x1, x2)
	potential = np.zeros((N, N))
	return x1, x2, x, y, potential

def integ(a1, a2, a3, x_min, x_max, y_min, y_max, N):
	""" Вычисление потенциала вращающегося трёхосного эллипсода в плоскости z=0 через интеграл """
	import numpy as np
	import math
	import scipy.integrate

	x1, x2, x, y, potential = grid(x_min, x_max, y_min, y_max, N)
	for i in range (N):

		for j in range (N):
			lam = ( math.sqrt( (a1**2 + a2**2 - x1[i]**2 - x2[j]**2)**2 - 4*(a1**2* a2**2 - x1[i]**2 * a2**2 - x2[j]**2 * a1**2) ) - (a1**2 + a2**2) ) / 2
			#print (lam)
			f = lambda v: (1 - (x1[i]**2 / (a1**2 + v)) - (x2[j]**2 / (a2**2 + v)) ) / math.sqrt((a1**2 + v) * (a2**2 + v) * (a3**2 + v))
			integral = scipy.integrate.quad(f, lam, np.inf)[0]
			potential[i, j] = 3/4*math.sqrt(a1**2 - a3**2)*integral
	return x, y, potential

def plot(x, y, potential):
	""" Построение графика функции потенциала Potential = f(x,y) в плоскости z=0 """
	import matplotlib.pyplot as plt

	fig = plt.figure()
	graph = fig.add_subplot(xlabel='X', ylabel='Y',zlabel='Potential', projection='3d')
	graph.plot_surface(x, y, potential	, cmap = 'jet')

	plt.show()
	plt.close()

def main():

	a1, a2, a3, x_min, x_max, y_min, y_max, N = enter()
	check(a1, a2, a3, x_min, x_max, y_min, y_max)

	if check(a1, a2, a3, x_min, x_max, y_min, y_max) == True:
	    grid(x_min, x_max, y_min, y_max, N)
	    x, y, potential = integ(a1, a2, a3, x_min, x_max, y_min, y_max, N)
	    plot(x, y, potential)

#main()
