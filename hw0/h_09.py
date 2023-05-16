"""
9. Сумма в прямоугольнике
"""
def get_ps2(a2):
	def get_ps1(a1):
		n = len(a1)
		ps1 = [0] * (n + 1)
		for i in range(n):
			ps1[i + 1] = ps1[i] + a1[i]
		return ps1

	n = len(a2)
	m = len(a2[0])
	ps1 = [0] * n
	for i in range(n):
		ps1[i] = get_ps1(a2[i])
	ps2 = [[0] * (m + 1) for _ in range(n + 1)]
	for j in range(1, m + 1):
		for i in range(n):
			ps2[i + 1][j] = ps2[i][j] + ps1[i][j]
	return ps2

n, m, k = map(int, input().split())
ps = get_ps2(tuple(tuple(map(int, input().split())) for i in range(n)))

for j in range(k):
	x1, y1, x2, y2 = map(int, input().split())
	print(ps[x2][y2] - ps[x2][y1-1] - ps[x1-1][y2] + ps[x1-1][y1-1])

"""
1) Префиксные суммы
Time O(N*M + K)
Memory O(N*M)

вычисляем преф.суммы для каждой строки
на основании них вычисляем преф.суммы для матрицы
отвечаем на каждый из K запросов за O(1)
"""