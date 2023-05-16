"""
10. Скучная лекция
"""
s = input()
n = len(s)

counter = {}
for i, letter in enumerate(s, 1):
	if letter not in counter:
		counter[letter] = 0
	counter[letter] += i + i*(n - i)

for letter in sorted(counter.keys()):
	print("{0}: {1}".format(letter, counter[letter]))

"""
1) String, Hash Table
Time O(n + 26*log(26) + 26)=O(n)
Memory O(26)=O(1)

счётчик (сколько раз встречается символ)
сначала сколько раз встречается, если будем удалять с начала 0(слово целиком),1,2 и т.д. символов
+на каждое первое действие будем удалять с конца 1,2 и т.д. символов
"""