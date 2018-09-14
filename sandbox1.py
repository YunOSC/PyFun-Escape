

expr = '''
def func({0}):
    c = a + b
    return c
print(func(10, 12) == 22)'''

if __name__ == '__main__':
    while True:
        print(expr.format('___________'))
        userInput = input('> ')
        print(expr.format(userInput))
        exec(expr.format(userInput))

