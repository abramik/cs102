#16

a = str(input())
a = int(a, 12)
b = []
while a > 0:
	if a % 14 == 10:
		b += 'A'
	elif a % 14 == 11:
		b += 'B'
	elif a % 14 == 12:
		b += 'C'
	elif a % 14 == 13:
		b += 'D'
	else:
		b += str(a % 14)
	a = a // 14
b = b[::-1]
b = "".join(map(str, b))
print(b)
