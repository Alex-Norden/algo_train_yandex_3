"""
1. Гистограмма
"""
import sys
from collections import defaultdict

counter = defaultdict(int)
max_count = 0

for line in sys.stdin:
	for char in line.strip():
		if char != " ":
			counter[char] += 1
			max_count = max(max_count, counter[char])

items = sorted(counter.items())
n = len(items)

for row_index in range(max_count, 0, -1):
	res = []
	for i in range(n):
		count = items[i][1]
		res.append("#" if row_index <= count else " ")
	print("".join(res))

print("".join(items[i][0] for i in range(n)))

"""
1) String
Time O(len(text))
Memory O(len(set(chars)))=O(1)

найти максимум
вывод сверху
"""