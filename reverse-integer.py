x = 123
x = -123
x = 120
x = 0

if x >= 0:
    x = str(x)[::-1]
else:
    x = "-"+str(x)[1:][::-1]
x = int(x)
if x >= -2**31 and x <= 2**31 -1:
    pass
else:
    x = 0

print(x)
