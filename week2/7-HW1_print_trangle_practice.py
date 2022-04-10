t = input()
t = int(t)
for i in range(t):
    # use i as border limitation
    # in the inner loop, print "t" without newline
    # after the inner loop, print "t\n"
    for j in range(i):
        print("t", end="")
    print("t")


t = input()
t = int(t)
for i in range(t):
    # use i+1 as border limitation
    # in the inner loop, print "t" without newline
    # after the inner loop, print "\n"
    for j in range(i+1):
        print("t", end="")
    print("")

t = input()
t = int(t)
for i in range(t, 0, -1):
    for j in range(i):
        print("t", end="")
    print("")


t = input()
t = int(t)
for i in range(t):
    for j in range(t-i):
        print("t", end="")
    print("")


t = input()
t = int(t)
for i in range(t):
    if i+1 != t:
        for j in range(t-i-1):
            print(" ", end="")
    for j in range(i+1):
        print("t", end="")
    print("")
