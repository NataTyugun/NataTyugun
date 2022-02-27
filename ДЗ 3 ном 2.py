import random
def password()->str:
    newpass = ' '
    k = random.randint(7,10)
    for i in range(k):
        newpass = newpass + chr(random.randint(33, 126))
    return newpass
print(password())
