"""
31. Поиск в глубину
"""
n, m = map(int, input().split())

from collections import defaultdict
g = defaultdict(set)

def dfs():
	start_v = 1
	stack = [start_v]
	visited = set()
	comp = []

	while stack:
		u = stack.pop()
		if u not in visited:
			visited.add(u)
			comp.append(u)
			stack.extend(g[u])

	comp.sort()
	print(len(comp))
	print(*comp)

for _ in range(m):
	u, v = map(int, input().split())
	if u == v:
		continue

	g[u].add(v)
	g[v].add(u)

dfs()

"""
1) Обход графов в глубину (DFS)
Time O(n+m)
Memory O(n+m)
	т.к. храним граф в списке смежности, для матрицы было бы n**2

при вводе петли пропускаем
кратные ребра сами перезапишутся
"""