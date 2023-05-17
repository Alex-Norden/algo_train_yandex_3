"""
19. Хипуй
"""
class Heap:
	def __init__(self):
		self._nodes = []

	def up(self, index):
		i = index
		while i > 0:
			parent = i // 2
			if self._nodes[parent] < self._nodes[i]:
				return
			self._nodes[parent], self._nodes[i] = self._nodes[i], self._nodes[parent]
			i = parent

	def down(self, index):
		size = len(self._nodes)
		if size == 1:
			return
		parent = index
		while True:
			l = 2 * parent
			if l >= size:
				break
			r = l + 1
			if r < size and self._nodes[r] < self._nodes[l]:
				l += 1
			if self._nodes[parent] < self._nodes[l]:
				return
			self._nodes[parent], self._nodes[l] = self._nodes[l], self._nodes[parent]
			parent = l

	def add(self, element):
		self._nodes.append(element)
		self.up(len(self._nodes) - 1)

	def pop(self):
		last = self._nodes.pop()
		if not self._nodes:
			return last
		res = self._nodes[0]
		self._nodes[0] = last
		self.down(0)
		return res


h = Heap()

for i in range(int(input())):
	s = input()
	if s == "1":
		print(-h.pop())
	else:
		h.add(-int(s.split()[1]))

"""
1) Очередь
Time O(n*log(n))
Memory O(n)
"""