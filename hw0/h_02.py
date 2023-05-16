"""
2. Красивая строка
"""
k = int(input())
s = input()
n = len(s)

def calc_max_len(char):
	max_len = 1
	count = 0
	l = 0
	r = 0

	while r < n:
		if s[r] != char:
			count += 1

		while count > k:
			if s[l] != char:
				count -= 1
			l += 1

		max_len = max(max_len, r - l + 1)
		r += 1

	return max_len

max_len = 1
ord_0 = ord("a")

for _ in range(26):
	max_len = max(max_len, calc_max_len(chr(ord_0)))
	ord_0 += 1

print(max_len)

"""
1) Два указателя
Time O(26*n)=O(n)
Memory O(1)

методом двух указателей находим максимальную подпослед-ть с определённым символом
"""