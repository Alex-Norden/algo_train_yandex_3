"""
17. Игра в пьяницу
"""
from collections import deque

q1 = deque(map(int, input().split()))
q2 = deque(map(int, input().split()))
i = 0
limit = 10**6

while q1 and q2:
	i += 1

	num1 = q1.popleft()
	num2 = q2.popleft()

	if num1 == 0 and num2 == 9:
		first = True
	elif num1 == 9 and num2 == 0:
		first = False
	else:
		first = num1 > num2

	if first:
		q1.append(num1)
		q1.append(num2)
	else:
		q2.append(num1)
		q2.append(num2)

	if not q1:
		print("second", i)
		break

	if not q2:
		print("first", i)
		break

	if i > limit:
		print("botva")
		break

"""
1) Очередь
Time O(n)
Memory O(n)

эмулируем игру
у кого не осталось карт, проигрывает
когда количество ходов перевалит за 10**6, останавлием
"""