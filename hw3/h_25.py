"""
25. Гвоздики
"""
n = int(input())
coords = list(map(int, input().split()))

coords.sort()

len_dp = n + 1
dp = [0]*len_dp
dp[1] = float("inf") #base DP

for i in range(2, len_dp):
	j = i-1
	len_last = coords[j] - coords[j-1]
	len_min = min(dp[i-1], dp[i-2])
	dp[i] = len_min + len_last

print(dp[n])

"""
1) ДП
Time O(n*log(n))
	sort
Memory O(n)

dp[i] миним. длина нитей до i-го гвоздя включительно
до i-го гвоздя обязательно тянуть
а дальше смотрим до i-1 или i-2 длина нитей была короче
"""