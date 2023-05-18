"""
22. Кузнечик
"""
n, k = map(int, input().split())
dp = [0] * n
dp[0] = 1 #base DP
for i in range(1, n):
	sm = 0
	j_start = max(0, i - k)
	for j in range(j_start, i):
		sm += dp[j]
	dp[i] = sm

print(dp[n - 1])

"""
1) ДП
Time O(n*k)
Memory O(n)

без рамки
суммируем предыдущие K (или меньше, если левее нет)
"""