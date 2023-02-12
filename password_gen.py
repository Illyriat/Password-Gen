import random
from tokenize import Special

#A Password genorator of 10 characters

#based on ASCII code, the following is randomly generated from it's range
lowercase = chr(random.randint(97,122))
lowercase2 = chr(random.randint(97,122))
lowercase3 = chr(random.randint(97,122))
uppercase = chr(random.randint(65,90))
uppercase2 = chr(random.randint(65, 90))
specialchr = chr(random.randint(33, 38))
specialchr2 = chr(random.randint(33, 38))
number = chr(random.randint(48, 57))
number2 = chr(random.randint(48, 57))
number3 = chr(random.randint(48, 57))


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Generate a password, then randomly place them in an order.
password = uppercase + lowercase + specialchr + number + number2 + uppercase2 + lowercase2 + specialchr2 +number3 + lowercase3
password = shuffle(password)

print("Here is your 10 Character Password. Keep it secret! Keep it safe! " + password)