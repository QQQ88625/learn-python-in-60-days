# square
x = input()
x = int(x)
for i in range(x):
    for j in range(x):
        print("x", end='')
    #print("\n", end='')
    print("")

# triangle
y = input()
y = int(y)
for i in range(y):
    for j in range(i+1):
        print(j, end='')
    print("")

# rectangle
width = int(input())
length = int(input())

for i in range(length):
    for j in range(width):
        print(j, end="")
    print('')

# different input method, instead of "entering number seperately"
text = "hello, world, ian, chi"
text = text.split("i")
print(text)
text = input()
print("text is \"{}\"".format(text))

text = text.split(" ")
print(text)

width, length = int(text[0]), int(text[1])
print(width, length)