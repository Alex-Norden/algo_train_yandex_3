"""
37. Путь в графе
"""
from collections import deque

n = int(input())

sz = n + 1
grid = [[0]*sz for _ in range(sz)]
for i in range(1, sz):
	for j, val in enumerate(map(int, input().split()), 1):
		grid[i][j] = val

start_v, end_v = map(int, input().split())

queue = deque([start_v])
dist = [-1] * sz
h = 0
dist[start_v] = h
parents = [None] * sz

while queue:
	h += 1
	for count in range(len(queue)):
		v0 = queue.popleft()
		for to in range(1, sz):
			if grid[v0][to]: #edge
				if dist[to] == -1: #undefined
					dist[to] = h #==dist[v0] + 1
					parents[to] = v0
					queue.append(to)

l = dist[end_v]
print(l)
if l > 0:
	path = [end_v]
	parent = parents[end_v]

	while parent is not None:
		path.append(parent)
		parent = parents[parent]

	path.reverse()
	print(*path)

"""
1) Обход графов в ширину (BFS)
Time O(n**2)
Memory O(n**2)

волновой алгоритм
"""