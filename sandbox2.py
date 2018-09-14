
expr = '''
def func({0}):
    c = a + b
    return c
print(func(10, 12) == 22)'''

if __name__ == '__main__':
    while True:
        print(expr.format('___________'))
        userInput = input('> ')
        if '__import__' in userInput:
            print('Illegal use! (__import__)')
        else:
            print(expr.format(userInput))
            exec(expr.format(userInput))

