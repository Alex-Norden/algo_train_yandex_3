"""
39. Путь спелеолога
"""
from collections import deque

n = int(input())

grid = [[[None]*n for _ in range(n)] for _ in range(n)]
start_v = None
for x in range(n):
	input() #skip
	for y in range(n):
		for z, char in enumerate(input()):
			if char == "S":
				start_v = (x,y,z)
			grid[x][y][z] = bool(char != "#") #free

def solution():
	queue = deque([start_v])
	h = 0
	x, y, z = start_v
	dist = [[[None]*n for _ in range(n)] for _ in range(n)]
	dist[x][y][z] = h

	dirs = [
		(-1,0,0),
		(1,0,0),
		(0,-1,0),
		(0,1,0),
		(0,0,-1),
		(0,0,1)
	]

	while queue:
		h += 1
		for _ in range(len(queue)):
			x0, y0, z0 = queue.popleft()
			for dx, dy, dz in dirs:
				x = x0 + dx
				y = y0 + dy
				z = z0 + dz
				if (-1 < x < n) and (-1 < y < n) and (-1 < z < n): #valid
					if grid[x][y][z] and dist[x][y][z] is None: #free and undefined
						if x == 0:
							return h

						dist[x][y][z] = h
						queue.append((x,y,z))

print(solution())

"""
1) Обход графов в ширину (BFS)
Time O(n**3)
Memory O(n**3)

волновой алгоритм
каждая клетка посещается не более одного раза
"""