# Завдання 2. Додати файл py_charm.py.
# Виконати аналогічні дії, як і у Завданні 1, крім створення гілки test
# Вирішити конфлікти.


# Функція, яка буде рахувати тільки позитивні числа.
def count():
    if a <= 0 or b <= 0:
        print('Enter only a positive numbers and not 0!')
    else:
        return a + b


'''
Закомітив функцію, створену у гілці test, оскільки виник конфлікт злиття.
'''
# Функція, яка буде рахувати тільки негативні числа.
# def count():
#     if a >= 0 or b >= 0:
#         print('Enter only a negative numbers and not 0!')
#
#         return 'Not correct value'
#     else:
#         return a + b

# a = -25
# b = -35

a = 25
b = 35


# Викликаю функцію
print(f'You entered: {a} and {b}')
print(f'{a} + {b} =', count())
