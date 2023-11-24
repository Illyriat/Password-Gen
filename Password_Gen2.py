#contains digits, ASCII letters, and special characters
import string

#used for generating strong random numbers and letters
import secrets

punked = string.punctuation

#some password feilds don't let you use certain characters so the following 
# variable is storing the ones that are most commonly not allowed to be used.
bad_punks = ['^', ':',  '~', '|', '[', ']', '{', '}', '`']
#test_string that takes that list and filters them out of 
# the selection before it heads to the password variable.
test_string = ''.join((filter(lambda i: i not in bad_punks, punked)))

#creating a variable called password using the import string as it's value
password = string.ascii_letters + test_string + string.digits

def make_password(length):
    return ''.join(secrets.choice(password) for i in range(length))



#printing 4 randomly generated passwords to the terminal for a user to choose from.
print("Your 8 character password is... " + make_password(8) + "  Keep it secret! Keep it safe!")
print("Your 10 character password is... " + make_password(10) + "  Keep it secret! Keep it safe!")
print("Your 12 character password is... " + make_password(12) + "  Keep it secret! Keep it safe!")
print("Your 16 character password is... " + make_password(16) + "  Keep it secret! Keep it safe!")