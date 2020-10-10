import matplotlib.pyplot as plt
import formula as fm
from numpy import arange
import random as rd
from fractions import Fraction as ft

def main():
	a = [ft(i) for i in range(18)]
	b = [ft(2 ** int(i) % 19) for i in a]
	n = fm.formula(a, b)
	d = n.cclt()
	na = list(arange(a[0], a[-1], 0.1))
	nb = [n.cp(d, i) for i in na]
	print(n.rstr(d, len(d)))
	plt.plot(na, nb) 
	plt.show()


if __name__ == "__main__":
	main()



