

import random
List = ['самовар', 'весна', 'лето']
word=list(random.choice(List))
letter=random.choice(word)
i=word.index(letter)
word[i]='?'
print(''.join(word))
unswer = input("Введите букву ")
if unswer==letter:
    print("Победа!")
    word[i]=letter
    print("Слово: "+''.join(word))
else:
    print("Увы!Попробуйте еще раз")
    word[i]=letter
    print("Слово: "+''.join(word))
