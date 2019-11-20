'''
 Форматированный ввод/вывод данных
'''
m = 10
pi = 3.1415927
print("m = ",m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m,pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")
code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space: ").split()
d, m, y = input("Enter three numbers splitted by \'.\': ").split('.')
print("{} + {} = {}".format(n1,n2,float(n1)+float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d,m,y,int(code)) )

m = 10
pi = 3.1415927
print("m = %4d" % m)
print("pi = %.3f" % pi)

year = input("Введите номер Вашего курса: ")
print(year)

r1, r2, r3 = input("ВВедите значения Ваших баллов ЕГЭ по русскому языку, математике и профильному предмету через запятую: ").split(',')
print("\n")

k = input("Введите 12-разрядное число в 12-ричной СС: ")
print("Исходное число: ", k)
print("Число в 10-тичной СС: ", int(k, 12))
print("\n")


j = int(input("Введите число: "))
print("Ваше число: ", j)
print("Ваше число * 2: ", j<<1)
z = int(input("Введите число: "))
print("Ваше число: ", z)
print("Ваше число / 2: ", z>>1)
print("\n")
