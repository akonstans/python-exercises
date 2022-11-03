# You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it).
#  If price for a movie per day is 3 dollars, how much will you have to pay?

lm = 3 * 3
bb = 5 *3
h = 1*3
print(lm  + h + bb)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
g = 400 * 6
f = 350 * 10
a = 380 * 4
print(g + a + f)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

class_has_space = True
student_has_time = True

enroll = class_has_space and student_has_time
print(enroll)

#A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.

offer = True
item_amount = 0
premium_member = True
apply_offer = offer and item_amount > 2 or premium_member
print(apply_offer)

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'
password_len = len(password)
username_len = len(username)
white_space = ?!.*\s
valid_id = password_len >= 5 
and username_len < 20 
and password != username 
and password.strip(-1) 
and username.strip(0)
and not white_space
print(valid_id)