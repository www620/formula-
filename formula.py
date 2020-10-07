class formula():
	def __init__(self, a, b):
		self.a = a#数组a
		self.b = b#数组b
		self.c = [1]#缓存数组c
		self.d = []#结果数组d
		self.i = 0#位置

	def add(self):
		n = (self.b[self.i] - self.cp(self.d, self.a[self.i]))\
			/ self.cp(self.c, self.a[self.i])
		self.d.append(0)
		for i in range(self.i):
			self.d[self.i - i] = self.d[self.i - i - 1]

		self.d[0] = 0
		for i in range(self.i + 1):
			self.d[self.i - i] += self.c[self.i - i] * n

		self.c.append(0)
		for i in range(self.i + 1):
			self.c[self.i - i + 1] -= self.c[self.i - i] * self.a[self.i]
		
		self.i += 1

	def cp(self, c, x):
		n = 1
		y = 0
		l = len(c)
		for i in range(l):
			y += c[l - i - 1] * n
			n *= x
		return y

	def cclt(self):
		for i in self.a:
			self.add()
		return self.d

	def rstr(self, d, l):
		string = ''
		for i in range(l):
			if (d[i]):
				if str(d[i])[0] != '-' and i:
					string += '+'
				if (d[i] != 1 and d[i] != -1 or l - i == 1):
					string += str(d[i])
				if l - i - 1:
					string += '*x'
					if l - i > 2:
						string += '^%d' % (l - i - 1)
		return string

if __name__ == "__main__":
	n = formula([1, 2, 3], [1, 2, 4])
	#n = formula(list(range(1, 9)), [1, 2, 3, 4, 6, 7, 8, 9])
	l = n.cclt()
	print(n.rstr(l, len(l)))