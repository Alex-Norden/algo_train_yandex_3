"""
40. Метро
"""
n = int(input())
m = int(input())

L = [None]*m
for i in range(m):
	_, *st_nums = map(int, input().split())
	L[i] = set(st_nums)

a, b = map(int, input().split())

def sol():
	curr_st_nums = set([a])
	for step in range(m):
		next_st_nums = set(curr_st_nums)
		for i in range(m):
			if curr_st_nums.intersection(L[i]):
				next_st_nums.update(L[i])

		if b in next_st_nums:
			print(step)
			return

		curr_st_nums = set(next_st_nums)

	print(-1)

sol()

"""
1) Обход графов в ширину (BFS)
Time O(m*(n/2) + m(n+m(2*n+2*n)))=O(m*n + m*n + n*m**2)=O(n*m**2)
Memory O(m*(n/2))=O(m*n)

волновой алгоритм
L[i] множество станций i-ой линии метро
если 2 линии метро имеют хоть одну общую станцию, то расширяем множество доступных станций next_st_nums (объединение множеств)
если конечная станция оказалась в множестве доступных, то останавливаемся
"""