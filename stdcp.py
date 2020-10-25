from formula import formula as fm
from fractions import Fraction as ft

a = []
b = []
n = input()
a = [ft(i) for i in n.split(' ')]
n = input()
b = [ft(i) for i in n.split(' ')]
d = fm(a, b)
d.cclt()
print(d.rstr(d.d, len(d.d)))
while True:
	print()
	n = input()
	print(d.cp(d.d, ft(n)))
