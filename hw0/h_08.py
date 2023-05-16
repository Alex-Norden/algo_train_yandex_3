"""
8. Минимальный прямоугольник
"""
k = int(input())
x_min = y_min = 10**10
x_max = y_max = -x_min
for i in range(k):
	x, y = map(int, input().split())
	x_min = min(x_min, x)
	y_min = min(y_min, y)
	x_max = max(x_max, x)
	y_max = max(y_max, y)
print(x_min, y_min, x_max, y_max)

"""
1) Math
Time O(k)
Memory O(1)

на каждом шаге определяем левый нижний (x_min, y_min) и правый верхний (x_max, y_max)
"""