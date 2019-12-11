#15

a = str(input())
a = int(a, 16)
negative = False
if a < 0:
	negative = True
b = []
for _ in range(7):
    b += str(abs(a) % 2)
    a = abs(a) // 2
b = b[::-1]
b = ['0'] + b
if negative:
	for i in range(8):
		if b[i] == '0':
			b[i] = '1'
		else:
			b[i] = '0'
	if b[7] == '0':
		b[7] = '1'
	else:
		b = b[::-1]
		i = 0
		while b[i] != '0':
			b[i] = '0'
			i += 1
		b[i] = '1'
		b = b[::-1]
b = "".join(map(str, b))
print(b)
