"""
12. Правильная скобочная последовательность
"""
d = {
	"(": ")",
	"[": "]",
	"{": "}"
}

stack = []
flag = True

for x in input():
	if x in d:
		stack.append(x)
	else:
		if stack:
			if d[stack.pop()] != x:
				flag = False
				break
		else:
			flag = False
			break

if flag:
	if stack:
		flag = False

print("yes" if flag else "no")

"""
1) Стек
Time O(n)
Memory O(n)

если открывающая
	добавляем в стек
иначе закрывающая
	достаём из стека и проверяем на соответствие
в конце проверяем, что в стеке не осталось открывающих
"""