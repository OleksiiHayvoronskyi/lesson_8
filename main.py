# Завдання 1. Створити репозиторій, додати файл main.py, у файлі створити
# функцію main_function(), додати код. Послідновно додати 3 коміти
# у гілці master після додавння трьох рядків коду.
# Створити і переключитися на гілку test, створити функцію test_function(),
# додати код. Послідновно додати 2 коміти у гілці test.
# Виконати шляхом злиття об’єдання гілок master і test. Git повідомить
# про конфлікт. Вирішити конфлікт. Зробити коміт у гілці master.


# Функція, яка рахує числа Фібоначчі.
def main_function(n):
    if n < 0:
        print('Not correct value')
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    # '''Далі ще буде 2 рядки коду'''
    else:
        return main_function(n - 1) + main_function(n - 2)


# Виведе перші 10 чисел ряду Фібоначчі.
print('--- 1st part of Task 1 ---')
print([main_function(n) for n in range(15)])


# Завдання 1. Продовження у гілці test.
# Функція у гілці test.

def test_function(name, massage):
    print('\n--- 2nd part of Task 1 ---')
    print(f'Hello, new branch {name}!')
    print(f'{massage}')


test_function('"test"', 'I am glad to see you in PyCharm.')

'''
Конфлікт злиття, який виник через зміну однакової частину коду у обох гілках,
вирішив через внесення вручну правок у код.
Потім командами: git add . та git commit -m, вніс у гілку майстер 
відповідні корективи. Знову виконав команду: git merge test
'''
