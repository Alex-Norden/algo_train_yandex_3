"""
27. Вывести маршрут максимальной стоимости
"""
n, m = map(int, input().split())
a = tuple(tuple(map(int, input().split())) for _ in range(n)) #matrix

n_dp = n + 1
m_dp = m + 1
dp = [[-1]*m_dp for _ in range(n_dp)]
dp[0][1] = 0 #base DP

prev = {}

for i in range(1, n_dp):
	for j in range(1, m_dp):
		if dp[i-1][j] > dp[i][j-1]: #down
			max_profit = dp[i-1][j]
			prev[(i, j)] = (i-1, j)
		else: #right
			max_profit = dp[i][j-1]
			prev[(i, j)] = (i, j-1)

		dp[i][j] = max_profit + a[i-1][j-1]

print(dp[n][m])

#---find path
path = []
while i > 1 or j > 1:
	i0, j0 = prev[(i, j)]
	if i - i0: #down
		path.append("D")
	else: #right
		path.append("R")
	i, j = i0, j0

path.reverse()
print(*path, sep=" ")

"""
1) ДП
Time O(n*m)
Memory O(n*m)

dp[i,j] макс-я стоимость маршрута до i,j включительно
для удобства построим рамку (0 использовать нельзя, т.к. это допустимое значение)

для восстановления ответа будем запоминать координату откуда пришли в словарь(массив не подойдёт, т.к. данные разряжены)
по разнице координат определим шли вниз (D) или направо (R)
"""