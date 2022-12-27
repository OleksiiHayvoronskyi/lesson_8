# Завдання 1. Створити репозиторій, додати файл main.py, у файлі створити
# функцію main_function(), додати код. Послідновно додати 3 коміти
# у гілці master після додавння трьох рядків коду.
# Переключитися на гілку test, створити функцію test_function(), додати код.
# Послідновно додати 2 коміти у гілці test.
# Виконати шляхом злиття об’єдання гілок master і test. Git повідомить
# про конфлікт. Вирішити конфлікт. Зробити коміт у гілці master.


# Функція у гілці test.
def test_function(name, massage):
    print(f'Hello, new branch {name}!')
    print(f'{massage}')


test_function('"test"', 'I am glad to see you in PyCharm.')







