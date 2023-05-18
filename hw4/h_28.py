"""
28. Ход конём
"""
n, m = map(int, input().split())

dp = [[None]*m for _ in range(n)]
dp[0][0] = 1 #base DP

def _dp(i, j):
	if i > -1 and j > -1:
		return dp[i][j]
	return 0

for i in range(n):
	for j in range(m):
		if i == 0 and j == 0:
			continue
		dp[i][j] = _dp(i-2, j-1) + _dp(i-1, j-2)

print(dp[n-1][m-1])

"""
1) ДП
Time O(n*m)
Memory O(n*m)

dp[i][j] кол-во способов(маршрутов) попадания в клетку i,j включительно
без рамки
база 1 (стоим в начале)
суммируем оба варианта (если доступны)
"""