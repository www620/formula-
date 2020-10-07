import matplotlib.pyplot as plt
import formula as fm
from numpy import arange
from fractions import Fraction as ft

def main():
	a = [ft(i) for i in [1, 3, 4, 5]]
	b = [ft(i) for i in [1, 2, 3, 5]]
	n = fm.formula(a, b)
	d = n.cclt()
	na = list(arange(0, 9, 0.1))
	nb = [n.cp(d, i) for i in na]
	print(n.rstr(d, len(d)))
	plt.plot(na, nb) 
	plt.show()


if __name__ == "__main__":
	main()



