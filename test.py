from pseudofun.pseudocode import *

code = '''
REPEAT
    x <- x + 1
UNTIL x = 7
'''
print(get_model(code))
print(get_python(code))