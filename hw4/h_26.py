"""
26. Самый дешевый путь
"""
n, m = map(int, input().split())
cost = tuple(tuple(map(int, input().split())) for _ in range(n)) #matrix

INF = 10**3
n_dp = n + 1
m_dp = m + 1
dp = [[INF]*m_dp for _ in range(n_dp)]
dp[0][1] = 0 #base DP

for i in range(1, n_dp):
	for j in range(1, m_dp):
		dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i-1][j-1]

print(dp[n][m])

"""
1) ДП
Time O(n*m)
Memory O(n*m)

dp[i][j] миним. вес для попадания в клетку i,j включительно
создаём рамку из бесконечно большого штрафа

*для экономии памяти можно хранить лишь две строки стоимостей
"""