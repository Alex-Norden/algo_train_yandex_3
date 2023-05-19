"""
35. Поиск цикла
"""
n = int(input())

sz = n + 1
grid = [[0]*sz for _ in range(sz)]
for i in range(1, sz):
	for j, val in enumerate(map(int, input().split()), 1):
		grid[i][j] = val
visited = [0] * sz

def find_loop():
	def print_loop(parent, to):
		res = [parent]
		while True:
			parent = prevs[parent]
			res.append(parent)
			if parent == to:
				break
		print("YES")
		print(len(res))
		print(*res)

	prevs = {}
	def dfs(v0, parent):
		"""
		return true if detected loop
		"""
		visited[v0] = 1
		prevs[v0] = parent

		for to in range(1, sz):
			if grid[v0][to]:
				if not visited[to]:
					if dfs(to, v0):
						return True
				elif to != parent:
					print_loop(v0, to)
					return True

	for v0 in range(1, sz):
		if not visited[v0]:
			if dfs(v0, -1):
				return
	print("NO")

find_loop()

"""
1) Обход графов в глубину (DFS)
Time O(n**2)
Memory O(n**2)

для удобства добавим рамку из нулей (чтоб использовать оригинальную индексацию с 1)
если обнаружен посещённый сосед 'to', который не является нашим родителем
	найден цикл
	для восстановления будем идти назад до этой вершины 'to'
"""