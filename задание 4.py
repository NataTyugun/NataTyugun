name = input("Введите имя")
if len(name) < 5:
    surname = input("Введите фамилию")
    print (name.upper()+ surname.upper())
else:
    print(name.lower())
