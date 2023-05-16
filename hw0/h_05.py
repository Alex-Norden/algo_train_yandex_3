"""
5. Хорошая строка
"""
n = int(input())
res = 0
a = int(input())
for i in range(n - 1):
	b = int(input())
	res += min(a, b)
	a = b
print(res)

"""
1) Math
Time O(n)
Memory O(1)

буквы идут по порядку (a..z)
среди двух соседних (например, ab) выбираем минимальное количество
добавляем к ответу
"""