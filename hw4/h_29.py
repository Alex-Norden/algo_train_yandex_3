"""
29. Кафе
"""
n = int(input())
costs = [int(input()) for _ in range(n)]

m = n + 1
INF = 1000*n
dp = [[INF]*m for _ in range(m)]
dp[0][0] = 0 #base DP

def _dp(i, j):
	if -1 < i < m and -1 < j < m:
		return dp[i][j]
	return INF

for i in range(1, m):
	for j in range(m):
		cost = costs[i-1]
		variants = []

		dp1 = _dp(i-1, j-1)
		if cost > 100 and dp1 != INF:
			variants.append(dp1 + cost)

		dp2 = _dp(i-1, j)
		if dp2 != INF:
			variants.append(dp2 + cost)

		dp3 = _dp(i-1, j+1)
		if dp3 != INF:
			variants.append(dp3)

		if variants:
			dp[i][j] = min(variants) #rewrite
		else:
			break

# width = len(str(INF)) + 1
# for row in dp:
# 	for x in row:
# 		print(f"{x:<{width}}", end="")
# 	print()

#---find answer
min_val = INF
for j in range(m):
	if dp[n][j] < min_val:
		min_val = dp[n][j]

print(min_val)

#-----find k1
for j in range(m-1, -1, -1):
	if dp[n][j] == min_val:
		break
k1 = j

#-----find k2
day_list = []
now_val = min_val
for i in range(m-1, 0, -1):
	cost = costs[i-1]

	dp1 = _dp(i-1, j-1)
	if now_val == dp1 + cost:
		now_val = dp1
		j -= 1
		continue

	dp2 = _dp(i-1, j)
	if now_val == dp2 + cost:
		now_val = dp2
		continue

	dp3 = _dp(i-1, j+1)
	if now_val == dp3:
		j += 1
		day_list.append(i)

print(k1, len(day_list))
if day_list:
	day_list.reverse()
	print(*day_list, sep="\n")

"""
1) ДП
Time O(n**2 + n)=O(n**2)
Memory O(n**2)

минимизировать сумму при макс-м кол-ве купонов
dp[i,j] миним. стоимость первых i обедов, имея j купонов
база: в 0-й день, имея 0 купонов, потратили 0 руб

dp1 i-1, j-1 (если получаем купон)
dp2 i-1, j (не трогаем купон)
dp3 i-1, j+1 (тратим купон)

в качестве бесконечности задаём макс-ую стоимость всех обедов с запасом
восстанавливать ответ начинаем с последнего дня
находим миним. стоимость всех обедов с макс. кол-ом купонов на руках
далее "раскручиваем" динамику до нулевого дня
"""