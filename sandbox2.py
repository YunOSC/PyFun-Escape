
if __name__ == '__main__':
    while True:
        print('Please satisfied this python.')
        print('def fun(____________):')
        print('    c = a + b')
        print('    return c')
        print('print(func(10, 12) == 22)')
        userInput = input('> ')
        if '__import__' in userInput:
            print('Illegal use! (__import__)')
        else:
            expr = '''
def func({0}):
    c = a + b
    return c
print(func(10, 12) == 22)'''.format(userInput)
            print(expr)
            exec(expr)

