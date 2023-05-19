"""
32. Компоненты связности
"""
def find_comp(g, g_size):
	comp = []
	comps = []
	used = [False] * g_size

	def dfs(start_v):
		stack = [start_v]
		while stack:
			u = stack.pop()
			if not used[u]:
				used[u] = True
				comp.append(u)
				stack.extend(g[u])

	for i in range(1, g_size):
		if not used[i]:
			comp.clear()
			dfs(i)
			comps.append(list(comp))

	return comps


n, m = map(int, input().split())

g_size = n + 1
g = [set() for _ in range(g_size)]

for _ in range(m):
	u, v = map(int, input().split())
	g[u].add(v)
	g[v].add(u)

comps = find_comp(g, g_size)
print(len(comps))
for comp in comps:
	print(len(comp))
	print(*comp)

"""
1) Обход графов в глубину (DFS)
Time O(n+m)
Memory O(n+m)

для удобства добавим в граф нулевую строку (иначе пришлось бы делать смещение номеров вершин при вводе и выводе)
для поиска всех компонент связности будем из каждой вершины запускать обход, не очищая посещённые вершины
"""