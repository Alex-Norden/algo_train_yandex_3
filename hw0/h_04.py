"""
4. Контрольная работа
"""
n = int(input())
k = int(input())
i = int(input())
j = int(input())

place0 = (i - 1)*2 + j
places = []

place_back = place0 + k
if place_back <= n:
	i1, j1 = divmod(place_back + 1, 2)
	places.append((i1, j1 + 1))

place_front = place0 - k
if place_front > 0:
	i1, j1 = divmod(place_front + 1, 2)
	places.append((i1, j1 + 1))

if places:
	if len(places) == 1:
		print(*places[0])
	else:
		if places[0][0] - i <= i - places[1][0]:
			print(*places[0])
		else:
			print(*places[1])
else:
	print(-1)

"""
1) Math
Time O(1)
Memory O(1)

вычисляем место первого ученика
находим место позади, затем впереди
если возможное место одно, то вернуть
иначе
	если место сзади ближе или равноудаленно, то вернём его
	иначе - другое
возвращаем номер парты, место за партой
"""