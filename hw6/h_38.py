"""
38. Блохи
"""
from collections import deque

n, m, s, t, q = map(int, input().split())
n += 1
m += 1

def solution():
	dirs = [
		(2, -1),
		(2, 1),
		(-2, 1),
		(-2, -1),
		(1, 2),
		(1, -2),
		(-1, 2),
		(-1, -2)
	]

	queue = deque([(s,t)])
	h = 0
	dist = [[-1]*m for _ in range(n)]
	dist[s][t] = h

	while queue:
		h += 1
		for _ in range(len(queue)):
			i0, j0 = queue.popleft()
			for di, dj in dirs:
				i = i0 + di
				j = j0 + dj
				if 0 < i < n and 0 < j < m: #valid
					if dist[i][j] == -1: #undefined
						dist[i][j] = h
						queue.append((i, j))

	sm = 0
	for _ in range(q):
		i, j = map(int, input().split())
		if dist[i][j] == -1: #undefined
			sm = -1
			break
		sm += dist[i][j]
	print(sm)

solution()

"""
1) Обход графов в ширину (BFS)
Time O(n*m + q)
Memory O(n*m)

для удобства добавим рамку (чтоб использовать оригинальную индексацию с 1)
найдём расстояние от кормушки до всех клеток на доске
если известны все расстояния от позиций блох (достижимы), то просуммировать
"""