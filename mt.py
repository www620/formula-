import matplotlib.pyplot as plt
import formula as fm
from numpy import arange
from fractions import Fraction as ft

def main():
	a = [ft(i) for i in range(1, 9)]
	b = [ft(i) for i in [1, 2, 3, 4, 6, 7, 8, 9]]
	n = fm.formula(a, b)
	d = n.cclt()
	na = list(arange(0, 9, 0.1))
	nb = [n.cp(d, i) for i in na]
	for i in d:
		print(str(i), end = ' ')
	print()
	plt.plot(na, nb) 
	plt.show()


if __name__ == "__main__":
	main()



