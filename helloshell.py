Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> line 1 = 'Hello Python developer ...'
SyntaxError: invalid syntax
>>> 'Hello Python developer . . .'
'Hello Python developer . . .'
>>> 
>>> line1 = 'Hello Python developer . . .'
>>> line2 = 'Welcome to the world of Python!'
>>> print(line1)
Hello Python developer . . .
>>> print(line2)
Welcome to the world of Python!
>>> 
=============================== RESTART: Shell ===============================
>>> x = 3
>>> x
3
>>> 
=============================== RESTART: Shell ===============================
>>> x
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
>>> #basically restarting the python shell causes the value to not be recognized anymore.
>>> 
