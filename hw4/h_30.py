"""
30. НОП с восстановлением ответа
"""
n = int(input())
a = tuple(map(int, input().split()))
m = int(input())
b = tuple(map(int, input().split()))

n_dp = n + 1
m_dp = m + 1
dp = [[0]*m_dp for _ in range(n_dp)]
for i in range(1, n_dp):
	for j in range(1, m_dp):
		if a[i-1] == b[j-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for row in dp:
# 	print(*row)
# print(dp[n][m])

#---find ans
lcs = []
i, j = n, m
while i > 0 and j > 0:
	if a[i-1] == b[j-1]:
		lcs.append(a[i-1])
		i -= 1
		j -= 1
	elif dp[i-1][j] == dp[i][j]:
		i -= 1
	else:
		j -= 1

lcs.reverse()
print(*lcs)

"""
1) ДП
Time O(n*m + (n+m))=O(n*m)
	(n+m) для восстановления ответа, т.к. двигаемся в худшем случаем на шаг по i/j
Memory O(n*m)

dp[i,j] длина НОП на первом префиксе до i, втором до j
добавим рамку из 0-лей (нет общих подпосл-ей)

сравнимаем крайние на префиксе элементы
если равны, то dp[i,j] = dp[i-1,j-1] + 1
иначе dp[i,j] = max(dp[i-1,j], dp[i,j-1])
"""