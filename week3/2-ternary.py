a = int(input())
b = int(input())
c = int(input())


if a <= b :
    min = a if (a <= c) else c
else:
    min = b if (b <= c) else c 
    
print(min, "is the smallest")

# the " else if" statement
if a < 10:
    print("a < 10.")
else:
    if a >10:
        print("a > 10.")
    else:
        (print("a == 10."))
        
if a < 10:
    print("a < 10.")
elif a > 10:
    print("a > 10.")
else:
    print("a == 10.")
    
    
    