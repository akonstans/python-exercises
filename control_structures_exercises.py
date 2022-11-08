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
if num > 0:
    while num >= 1:
        print(num)
        num -= 1
        if num < 1:
            break
else:
    print('invalid number')

numby =input('positive number')
numby = int(numby)
o = 0
if numby > 0:
    while o <= numby:
        if numby > 0:
            print(o)
            o += 1
            if o > numby:
                break
else:
    print('invalid number')

odds = [x for x in range(50) if x % 2 == 1]


def odd_loop(start_at, end_at):
    for num in range(start_at, end_at + 1, 2):
        print(f'Here is an odd integer:{num:>3}')

def check_user_number():
    user_input = input('Enter an odd number less than 50: ')
    
    while True:
        if user_input.isdigit() == False:
            print(f'{user_input} is not a number')
            break

        user_input = int(user_input)
        
        if user_input not in odds:
            print(f'{user_input} is not an odd number')
            break
            
        if user_input > 1:
            odd_loop(1, user_input - 2)

        print(f'Yikes! Skipping number:{user_input:>3}')

        if user_input < 49:
            odd_loop(user_input + 2, 49)
            
        user_input = input('Enter another odd number less than 50: ')
        
check_user_number()

for num in range(1, 101):
    fibu = ''
    if num % 3 == 0:
        fibu += 'Fizz'
    if num % 5 == 0:
        fibu += 'Buzz'
    if not fibu:
        fibu = num
    print(fibu)

def square(i):
    return i*i
def cube(i):
    return i*i*i
  
def table():
    start = 1
    end=input("What number would you like to go up to? ")
    end = int(end)
    
    
    print("======\t\t=====\t\t=====")
    print("Number\t\tSquare\t\tCubed")
    print("======\t\t=====\t\t=====")
      
    for i in range(start,end+1):
        print(i,"\t\t",square(i),"\t\t",cube(i))
        
    while True:
        a = input("Continue? yes/no ")
        if a=="yes":
            print("Enter a new number")
            continue
        elif a=="no":
            print("Stopping")
            break
        else:
            print("Enter either yes/no")
table()
