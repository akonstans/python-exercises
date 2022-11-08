# First we need to import the students dictionary into our file
from students import students
# Now we can code

# How many students are there?
print(len(students))
num_students = len(students)
# How many students prefer light coffee? 
coffeepref = [n['coffee_preference'] for n in students if n['coffee_preference'] == 'light']
print(coffeepref.count('light'))
# For each type of coffee roast?
totalpref = [n['coffee_preference'] for n in students]
light = totalpref.count('light')
medium = totalpref.count('medium')
dark = totalpref.count('dark')
print(light, medium, dark)
# How many types of each pet are there?
horse_count = 0
cat_count = 0
dog_count = 0
pets = list(n['pets'] for n in students)
for n in range(len(pets)):
    i = pets[n]
    for x in i:
        if x['species'] == 'horse':
            horse_count += 1
        elif x['species'] == 'cat':
            cat_count += 1
        else:
            dog_count += 1

print(horse_count, cat_count, dog_count)
# How many grades does each student have? 
grades_amt = [len(n["grades"]) for n in students]
print(grades_amt)
# Do they all have the same number of grades?
## YES THEY DO
# What is each student's grade average
grade = [sum(n['grades'])/len(n['grades']) for n in students]
print(grade)
# How many pets does each student have?
# How many students are in web development? data science?
# What is the average number of pets for students in web development?
# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
# What is the most common type of pet for web development students?What is the average name length?
# What is the highest pet age for light coffee drinkers?