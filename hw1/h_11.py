"""
11. Стек с защитой от ошибок
"""
stack = []

while True:
	s = input()
	if s == "exit":
		print("bye")
		break

	if s == "pop":
		if stack:
			print(stack.pop())
		else:
			print("error")
	elif s == "back":
		if stack:
			print(stack[-1])
		else:
			print("error")
	elif s == "size":
		print(len(stack))
	elif s == "clear":
		stack.clear()
		print("ok")
	elif s.startswith("push"):
		stack.append(s.split()[1])
		print("ok")

"""
1) Стек
Time O(n)
Memory O(n)
"""