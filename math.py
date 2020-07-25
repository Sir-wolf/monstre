#!/usr/bin/python3

x = -10
add = 0.5
for k in range(40000000):

	y = (x**3)*(2*x+3)*(2-x)/(x**2+1)*(x-5)

	if y > 0 : 
		if y == 0:
			print("%d1.1 ++"%x)
		else: 
			print("%d1.1 ++"%x)
	else: 
		print("%d1.1 --"%x)
	x += add
