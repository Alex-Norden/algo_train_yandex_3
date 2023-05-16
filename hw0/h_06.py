"""
6. Операционные системы lite
"""
m = int(input())
n = int(input())

final_list = []
for i in range(n):
	a, b = map(int, input().split())
	for i in range(len(final_list) - 1, -1, -1):
		c, d = final_list[i]
		if a <= d and c <= b:
			del final_list[i]
	final_list.append((a, b))
print(len(final_list))

"""
1) Полный перебор
Time O(n**2)
Memory O(n)

использовать сортировку событий нельзя, т.к. важен исходный порядок установок!
перебираем отрезки
	перебираем рабочие
		если новый отрезок пересекается с рабочим
			удаляем рабочий
		добавляем новый к рабочим
"""