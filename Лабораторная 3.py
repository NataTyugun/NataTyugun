def todo_list():
    import json
    print('''Простой todo:
     1. Добавить задачу.)
     2. Вывести список задач.)
     3. Выход.''')
     command= int(input('Укажите число: '))
     
    while True:
        if command==1:
            task = input('Сформулируйте задачу: ')
            category = input('Добавьте категорию к задаче: ')
            time = input('Добавьте время к задаче: ')
            t = """Задача: {z} Категория: {c} Дата:  {t}"""
            ex = t.replace('{z}', exercise)
            ex = ex.replace('{c}', category)
            ex = ex.replace('{t}', time)
            with open('todo.json', 'w') as f:
                json.dump(ex, f)
        elif command==2:
            try:
                with open('todo.json') as f:
                    numbers = json.load(f)
                print(numbers)
            except Exception as e:
                print(e)
        else:
            print("Неверное обращение к todo")
        command = int(input('Укажите число: '))
    print('задачи сохранены в файл!') 
