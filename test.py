from pseudofun.pseudocode import *

code = '''
x <- 0
REPEAT
    x <- x + 1
UNTIL x = 7
PRINT x
x <- x + 1
PRINT x
'''
print(get_model(code))
print(get_python(code))
run(code)