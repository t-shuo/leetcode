x = 121
x = -121
x = 10
x = -101
x = 0

if x < 0 or (x % 10 == 0 and x != 0):
    print("edge case", False)
else:
    revertednum = 0
    while x > revertednum:
        revertednum = revertednum * 10 + x % 10
        x = x // 10
        print(revertednum)
        print(x)
    print(revertednum == x)
    print(revertednum // 10 == x)
    print(revertednum == x or revertednum // 10 == x)