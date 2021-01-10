#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

a = 23
print(add_integer(1, 2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(a, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(z))
except Exception as e:
    print(e)
try:
    print(add_integer(4, True))
except Exception as e:
    print(e)
try:
    print(add_integer(4, [12]))
except Exception as e:
    print(e)
try:
    print(add_integer(4, (4, 3)))
except Exception as e:
    print(e)
