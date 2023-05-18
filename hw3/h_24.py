"""
24. Покупка билетов
"""
n = int(input())

times = [None] * n
for i in range(n - 1, -1, -1): #reverse
	times[i] = tuple(map(int, input().split()))

len_dp = n + 1
dp = [0] * len_dp
dp[0] = 0 #base DP
dp[1] = times[0][0]


for i in range(2, len_dp):
	a, b, c = times[i-1]

	if i > 2:
		variants = [
			dp[i-1] + a,
			dp[i-2] + b,
			dp[i-3] + c
		]
	else:
		variants = [
			dp[i-1] + a,
			dp[i-2] + b
		]

	dp[i] = min(variants)

print(dp[n])

"""
1) ДП
Time O(n)
Memory O(n)

dp[i] миним. время покупки билетов i-тому и людям за ним

'развернём очередь' для того, чтобы идти с конца
"""