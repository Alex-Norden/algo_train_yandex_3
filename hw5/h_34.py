"""
34. Топологическая сортировка
"""
def top_sort(g):
	def dfs(v0):
		stack = [v0]
		while stack:
			v = stack.pop()
			visited[v] = 1 #gray

			for to in g[v]:
				if visited[to] == 1:
					return False
				if not visited[to]:
					stack.append(v)
					stack.append(to)
					break
			else: #without break, no childs or visited
				visited[v] = 2 #black
				res.append(v)
		return res

	res = []
	for v0 in range(1, sz):
		if not visited[v0]:
			if not dfs(v0):
				return False
	return res


n, m = map(int, input().split())

sz = n + 1
g = [set() for _ in range(sz)]
visited = [0] * sz

for _ in range(m):
	u, v = map(int, input().split())
	g[u].add(v)

res = top_sort(g)
if res == False:
	print(-1)
else:
	res.reverse()
	print(*res)

"""
1) Обход графов в глубину (DFS)
Time O(n+m)
Memory O(n+m)

т.к. граф ориентированный, то обратное ребро не нужно
начинаем просмотр вершины помечаем серым(1), заканчиваем - чёрным(2) и добавляем в результат
если сосед оказался серым, обнаружили цикл (топологическая сортировка невозможна)

если всё успешно, выводим результат в обратном порядке
"""