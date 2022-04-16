a = int(input())
b = int(input())
c = int(input())

if a <= b :
    if a <= c:
        print(a, "is the smallest")
    else:
        print(c, "is the smaillest")
else:
    if b <= c:
        print(b, "is the smallest")
              
    else:
        print(c, "is the smaillest")
        
# using a varible to simplify repeated sentences
min = 0
if a <= b:
    if a <= c:
        min = a
    else :
        min = c
else:
    if b <= c:
        min = b
    else:
        min = c
print(min, "is the smallest")

min = c
if a <= b:
    if a <= c:
        min = a
else:
    if b <= c:
        min = b
print(min, "is the smaillest")


mini = 0
maxi = 100
a = 10

if mini < a and a < maxi:
    print("a is between {} and {}".format(mini, maxi))
else:
    print("a is out of range")
