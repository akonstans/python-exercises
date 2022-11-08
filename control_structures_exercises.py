# Enter a day of the week
day = "Sunday"
if day == 'Monday':
    print('Today is Monday')
else:
    print('Its not Monday')

if day == ('Saturday'):
    print('Its the weekend')
elif day == ('Sunday'):
    print('Its the weekend')
else:
    print('Its a weekday')

hours = 60
rate = 45
overtime = hours - 40

paycheck = hours * rate
overtime_check = (overtime * 1.5 * rate) + ((hours - overtime)* rate)
if hours > 40:
    print(overtime_check)
else:
    print(paycheck)

i = 5
while i <= 15:
    print(i)
    i += 1

i = 0
while i <= 100:
    print(i)
    i+=2

i = 100
while i >= -10:
    print(i)
    i-=5

i = 2
while i <= 1000000:
    print(i)
    i = i ** 2

i = 100
while i >= 5:
    print(i)
    i -=5

n = 7

print ("The Multiplication Table of: ", n)    
for count in range(11):      
   print (n, 'x', count, '=', n * count)    


rows = 10


for i in range(rows):
    for n in range(i):
        print(i, end=" ")
    

    print("\n")


posint = 7

while posint >= 1:
    print(posint)
    posint -= 1
    if posint < 1:
        break

num = input('positive number')
num = int(num)
num = 8
while num >= 1:
    print(num)
    num -= 1
    if num < 1:
        break

numby =input('positive number')
numby = int(numby)
o = 0
numby = 5
if numby >= 0:
    print(range(o, numby))
else:
    print('invalid number')

