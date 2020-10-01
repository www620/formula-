class formula():
	def __init__(self, a, b):
		self.a = a#数组a
		self.b = b#数组b
		self.c = [1]#缓存数组c
		self.d = [a[0]]#结果数组d
		self.i = 0#位置

	def add(self):
		n = self.b[self.i] - cp(self.c, self.a[self.i])
		self.i += 1
		self.c.append(0)
		for i in range(self.i):
			self.c[self.i - i] = self.c[self.i - i - 1]
		self.c[0] = 0
		for i in range(self.i):
			self.c[i] -= self.c[i + 1] * self.a[self.i]
		
		n /= self.b[self.i] - cp(self.c, self.a[self.i])
		for i in range(self.i):
			self.d[i] += self.c[i] / n

	def cp(self, c, x):
		n = 1
		y = 0
		for i in c:
			y += i * n
			n *= x
		return y

	def cclt(self):
		for i in self.a:
			self.add()
		return self.d

