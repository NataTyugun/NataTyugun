import random
number = random.randint(1,10)
chislo = 0;
while number != chislo :
    chislo = int(input("Введите число "))
    if number == chislo:
        print("Победа!")
        break
    elif number > chislo :
        print('число больше' , chislo)
    else:
        print('число меньше' , chislo)

    
