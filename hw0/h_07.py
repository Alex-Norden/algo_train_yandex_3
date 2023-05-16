"""
7. SNTP
"""
SECONDS24H = 24*60*60

def get_seconds():
	h, m, s = input().split(":")
	return int(h)*60*60 + int(m)*60 + int(s)

def print_res(s):
	if s >= SECONDS24H:
		s -= SECONDS24H

	s = int(s + 0.5)

	m, s = divmod(s, 60)
	h, m = divmod(m, 60)

	print("{:02d}:{:02d}:{:02d}".format(h, m, s))

sec_a = get_seconds()
sec_b = get_seconds()
sec_c = get_seconds()
print_res(sec_b + (((sec_c + SECONDS24H) - sec_a) / 2 if sec_a > sec_c else (sec_c - sec_a) / 2))

"""
1) Math
Time O(1)
Memory O(1)

перевести всё в минимальные единицы измерения (секунды)
ответ вернуть в заданном формате
"""