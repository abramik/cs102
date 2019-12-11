'''
 Циклы
'''
# while
print("Numbers < 10 (while):")
i = 0
while (i<10):
    print(i, end=" ") # print in one line
    i += 1
print("\n")
# for
print("Numbers < 10 (for):")
for i in range(0,10):
    print(i, end=" ")
else:
    print("\nThe next number is 10\n")
# break
sum = 0
for i in range(0,100):
    if i > 10:
        print("\n We reached the end, final sum: ", sum)
        break
    sum += i
# continue
i = 0
while i<=15:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print("\n")
# pass
print("Let's print numbers again!")
for i in range(0,10):
    pass
    print(i, end=" ")
print("\n\n")

#5
for i in range(0,500):
    if i % 7 == 0:
        print(i, end=" ") 
else: 
    print("All numbers were printed!")

'''
while i >= 0 and i <= 500:
    if i % 7 == 0:
        print(i, end=" ") 
else: 
    print("All numbers were printed!")
''' 

#6
for i in range(0,500):
        if i == 300:      
            break
        if i % 7 == 0 and i % 14 != 0: 
            print(i, end=" ") 
print("All numbers were printed!")

'''
while i >= 0 and i <= 500:
        if i == 300:      
            break
        if i % 7 == 0 and i % 14 != 0: 
            print(i, end=" ") 
print("All numbers were printed!")
'''

#7
a = [ [1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4] ]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

print('\n')   

a = [ 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4 ]
i = 0
while i < len(a):
        print(a[i], a[i+1],a[i+2], a[i+3])
        i += 4

 
