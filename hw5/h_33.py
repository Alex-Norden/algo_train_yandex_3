"""
33. Списывание
"""
n, m = map(int, input().split())

sz = n + 1
g = [set() for _ in range(sz)]
visited = [False] * sz

for _ in range(m):
	u, v = map(int, input().split())
	g[u].add(v)
	g[v].add(u)

def check():
	def dfs(start_v, color):
		visited[start_v] = color
		for v in g[start_v]:
			if visited[v] == color:
				return False
			if not visited[v]:
				if not dfs(v, 3-color):
					return False
		return True

	for u in range(1, sz):
		if not visited[u]:
			if not dfs(u, 1):
				return False
	return True

print("YES" if check() else "NO")

"""
1) Обход графов в глубину (DFS)
Time O(n+m)
Memory O(n+m)

разделение графа/раскраска в 2 цвета/проверка на двудольность
visited будем хранить цвета (0 значит не просматривали)

*(3-color) хак для преобразования 1->2, 2->1
"""