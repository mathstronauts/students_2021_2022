>>> a_float = 3.141
>>> a_float
3.141
>>> a_int = int(a_float)
>>> a_int
3
>>> b_float = 3.9999
>>> b_float
3.9999
>>> b_int = int(b_float)
>>> b_int
3
>>> num = 12345
>>> print("some string" + num)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print("some string" + num)
TypeError: can only concatenate str (not "int") to str
>>> num_str = str(num)
>>> print("some string" + num_str)
some string12345
