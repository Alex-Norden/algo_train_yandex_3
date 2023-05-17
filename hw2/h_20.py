"""
20. Пирамидальная сортировка
"""
n = int(input())
h = list(map(int, input().split()))

def heapify(h_size, index):
	mx = index
	l = (2 * index) + 1
	r = l + 1

	if l < h_size and h[l] > h[mx]:
		mx = l

	if r < h_size and h[r] > h[mx]:
		mx = r

	if mx != index:
		h[index], h[mx] = h[mx], h[index]
		heapify(h_size, mx)

for i in range(n, -1, -1):
	heapify(n, i)

for i in range(n - 1, 0, -1):
	h[i], h[0] = h[0], h[i]
	heapify(i, 0)

print(" ".join(map(str, h)))

"""
1) Очередь
Time O(n*log(n))
Memory O(n)
"""