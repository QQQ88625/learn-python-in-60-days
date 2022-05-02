i = 0 
print(i < 10)

i = 0 
while True:
    x = input()
    if x != 'exit':
        pass
    else:
        break
    i += 1
    print(i, x)

for i in range(100):
    x = input()
    if x != 'exit':
        pass
    else:
        break
    print(i, x)