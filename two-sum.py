nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

h = {}
for i, num in enumerate(nums):
    n = target - num
    print(i, num, n)
    print(n not in h)
    if n not in h:
        h[num] = i
        print(h)
    else:
        print(h[n], i)
        #break
