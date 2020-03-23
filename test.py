from pseudofun.pseudocode import *

code = '''
FUNCTION noot x
    PRINT x
ENDFUNCTION
x <- a
x <- (a)
x <- (a h)
X <- (a ((h)))
x <- (a(f))
'''
print(get_model(code))
print(get_python(code))
run(code)