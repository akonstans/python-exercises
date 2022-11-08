# defining function
def is_two(n):
    # finding any way n could be two
    if n == 2 or n == '2' or n == 'two':
        #creating a boolean based on input
        return True
    else:
        return False
# end of function should return false if input is not 2


# defining function
def is_vowel(x):
    # any instance of a vowel using an if statement
    if x in '[aieouAIEOU]':
    # boolean setup to determine if it is or isnt a vowel
        return True
    else:
        return False
# end of function should determine if argument is a vowel or not

# defining function
def is_consonant(y):
    # using the function above we just invert it
    if is_vowel(x):
        return False
    else:
        return True
# end of function, now it should return true if string is not a vowel

# defining function
def caps_con(n):
    #using the function above we take the first letter of the string
    if is_consonant(n[0]):
    # if the first letter is a consanent it will capitalize it
        return(n.capitalize())
    else:
       return(n)
# end of function


# defining function
def calculate_tip(tip_percentage, cost):
    # using the two variables we can simple take cost
    # multiply it by proposed tip percentage in decimal form
    # if we wanted to use a number we could just divide tip by 100 first
    tip_cost = cost * tip_percentage
    return round(tip_cost, 2)
# end of function returns the total dollar amount of tip


# defining function
def apply_discount(price, discount):
    #creating a price and discount percent then basic math to find total cost
    final_price = price - (price * discount)
    return final_price
# end of function

# defining function
def handle_commas(n):
    #replaces all commas in a number with nothing 
    num = n.replace(',', '')
    return num
# end of function

# defining function
def get_letter_grade(n):
    if n <= 60:
        return 'F'
    elif n <= 70:
        return 'D'
    elif n <= 80:
        return 'C'
    elif n <= 90:
        return 'B'
    elif n <= 100:  
        return 'A'
# end of function, it finds a letter grade with the lowest grade taking priority
#using the if statements

# defining function
def remove_vowels(n):
    # return of is_vowel function and then simply replace any vowels with nothing
    for i in n:
        if is_vowel(i):
            n = n.replace(i, '')
    return n
# end of function

# defining function
def normalize_name(n):
# for every letter in n
    for i in n:
# if the instance is not alpha numeric replace it
        if i.isalnum() == False:
            n = n.replace(i, '')
# make it lower case
    n = n.lower()
# remove excess white space
    n = n.strip()
# replace spaces with underscores
    n = n.replace(' ', '_')
    return n
# end of function

# defining function    
def cumulative_sum(n):
# x starts at 0 to get an accurate sum
    x = 0
# creating a list to populate with the new values
    new_list = []
    for i in n:
        x += i
    # populate new list with the running sum
        new_list.append(x)
    return new_list
# end of function returning the cumulative sum of any integers input into the function