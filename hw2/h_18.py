"""
18. Дек с защитой от ошибок
"""
from collections import deque
q = deque()

while True:
	s = input()
	if s == "exit":
		print("bye")
		break

	if s == "pop_front":
		if q:
			print(q.popleft())
		else:
			print("error")
	elif s == "pop_back":
		if q:
			print(q.pop())
		else:
			print("error")
	elif s == "front":
		if q:
			print(q[0])
		else:
			print("error")
	elif s == "back":
		if q:
			print(q[-1])
		else:
			print("error")
	elif s == "size":
		print(len(q))
	elif s == "clear":
		q.clear()
		print("ok")
	elif s.startswith("push_front"):
		q.appendleft(s.split()[1])
		print("ok")
	elif s.startswith("push_back"):
		q.append(s.split()[1])
		print("ok")

"""
1) Очередь
Time O(n)
Memory O(n)
"""