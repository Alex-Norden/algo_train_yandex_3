"""
23. Калькулятор
"""
n = int(input())
len_dp = n + 1
dp = [0] * len_dp

for y in range(2, len_dp):
	x1 = y / 2
	x1 = int(x1) if x1 == int(x1) else None

	x2 = y / 3
	x2 = int(x2) if x2 == int(x2) else None

	x3 = y - 1

	prevs = [dp[x3]]
	if x1 is not None:
		prevs.append(dp[x1])

	if x2 is not None:
		prevs.append(dp[x2])

	dp[y] = min(prevs) + 1

print(dp[n])

y_last = n
ans = [y_last]
for y in range(n - 1, 0, -1): #[n-1..0)
	if dp[y] < dp[y_last] and (y+1==y_last or y*2==y_last or y*3==y_last):
		y_last = y
		ans.append(y_last)
ans.reverse()
print(*ans, sep=" ")

"""
1) ДП
Time O(n)
Memory O(n)

с сертификатом (восстановлением ответа)
по одной из трёх операций
определим наим. кол-во операций для X

идея:
проходим по всем числам Y до N
Y может быть получено умножением на 2,3 или инкрементом на 1
к предыдущему миним-му операций добавляем 1 (текущую)

при восстановлении ответа проверяем,что
	зн-е динамики меньше
	y_last могло быть получено одной их трёх операций
"""