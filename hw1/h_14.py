"""
14. Сортировка вагонов lite
"""
end = int(input())
start = 1
stack = []

for num in map(int, input().split()):
	while stack:
		if stack[-1] == start:
			start += 1
		elif num == end:
			end -= 1
		else:
			break
		del stack[-1]

	if num == start:
		start += 1
	elif num == end:
		end -= 1
	else:
		stack.append(num)

print("NO" if stack else "YES")

"""
1) Стек
Time O(n)
Memory O(n)

если есть вагоны в тупике (stack)
	пытаемся перегнать их в голову или хвост
если можем перегнать текущий в голову или хвост
	перегоняем
иначе
	запоминаем, что в тупике (stack)

*'перегнать в хвост' означает оставить в тупике и забыть до тех пор, пока вагоны не закончатся
"""