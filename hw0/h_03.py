"""
3. Коллекционер Диего
"""
n = int(input())
a = map(int, input().split())
k = int(input())
p = map(int, input().split())

a = list(set(a))
p = list((x, i) for i, x in enumerate(p))

a.sort()
p.sort()

ans = [0] * k
j = len(a) - 1

for i in range(k - 1, -1, -1):
	while j > 0 and a[j] >= p[i][0]:
		j -= 1
	if a[j] < p[i][0]:
		ans[p[i][1]] = j + 1

print(*ans, sep="\n")

"""
1) Два указателя
Time O(N*logN + K*logK)
Memory O(N+K)

идём от максимальных (справа)
пропускаем все наклейки, которые не интересуют коллекционеров
для каждого коллек-ра записываем сколько ему интересны (кол-во слева)
"""