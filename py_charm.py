# Функція, яка буде рахувати тільки позитивні числа.
def count():
    if a <= 0 or b <= 0:
        print('Enter only a positive numbers and not 0!')
        return 'Not correct value'
    else:
        return a + b


a = 25
b = 35

# Викликаю функцію
print(f'You entered: {a} and {b}')
print(f'{a} + {b} =', count())
