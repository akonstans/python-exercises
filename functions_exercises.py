def is_two(n):
    if n == 2 or n == '2' or n == 'two':
        return True
    else:
        return False




def is_vowel(x):
    if x in '[aieouAIEOU]':
        return True
    else:
        return False



def is_consonant(y):
    if is_vowel(x):
        return False
    else:
        return True



def caps_con(n):
    if is_consonant(n[0]):
        return(n.capitalize())
    else:
        return(n)



def calculate_tip(tip_percentage, cost):
    tip_cost = cost * tip_percentage
    return round(tip_cost, 2)
calculate_tip(.25, 50)



def apply_discount(price, discount):
    final_price = price - (price * discount)
    return final_price


def handle_commas(n):
    num = n.replace(',', '')
    return num



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


def remove_vowels(n):
    for i in n:
        if is_vowel(i):
            n = n.replace(i, '')
    return n

def normalize_name(n):
    for i in n:
        if i in '?!@$%><.,':
            n = n.replace(i, '')
    n = n.lower()
    n = n.strip()
    n = n.replace(' ', '_')
    return n
    
def cumulative_sum(n):
    x = 0
    new_list = []
    for i in n:
        x += i
        new_list.append(x)
    return new_list
