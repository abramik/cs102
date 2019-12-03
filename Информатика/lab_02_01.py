'''
 Условия
'''
# if..else
num = int(input("How many times have you been to the Hermitage? "))
if num > 0:
    print("Wonderful!")
    print("I hope you liked this museum!")
else:
    print("You should definitely visit the Hermitage!")
# if..elif..else
course = int(input("What is your course number?"))
if course == 1:
    print("You are just at the beginning!")
elif course == 2:
    print("You learned many things, but not all of them!")
elif course == 3:
    print("The basic course is over, it's time for professional disciplines!")
else:
    print("Oh! You need to hurry! June is the month of thesis defense")
x = 5
y = 12
if y % x > 0 : print("%d cannot be evenly divided by %d" % (y,x))
z = 3
x = "{} is a divider of {}".format(z,y) if y%z==0 else "{} is not a divider of {}".format(z,y)
print(x)
# в одну строку
p = int(input("Сколько лабораторных работ ты выполнил(а) за год? "))
v = 10
p = "Выполнено: {}, меньше чем {}".format(p,v) if p < v else "Выполнено: {}, больше чем {}".format(p,v)
print(p)
# в несколько строчек
r = int(input("Сколько лабораторных работ ты выполнил(а) за год? "))
if r > v:
    print("Количество выполненных рабораторных работ: %d" % (r))
else:
    print("Ты выполнил %d лабораторных работ или меньше" % (v))

a = 157
b = 525
if a > b : print(a % b)
elif a < b: print(b % a)
else : print(a * b)

print("\n\n")
