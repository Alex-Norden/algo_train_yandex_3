"""
15. Великое Лайнландское переселение
"""
n = int(input())
arr = list(map(int, input().split()))

stack = []
from collections import deque
q = deque()

for i in range(n - 1, -1, -1):
	while stack:
		if stack[-1][0] < arr[i]:
			q.appendleft(str(stack[-1][1]))
			break
		stack.pop()

	if not stack:
		q.appendleft("-1")

	stack.append((arr[i], i))

print(" ".join(q))

"""
1) Стек
Time O(n)
Memory O(n)

идея в том, чтобы хранить историю предыдущих значений и среди них искать меньшие, а большие удалять, т.к. не нужны
идём с конца
храним в стеке значения, которые меньше и правее текущего
"""