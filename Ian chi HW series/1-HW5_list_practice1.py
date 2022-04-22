# list[]
x = []
print(x)

x = [10, 100, 1000, 20, 200, 2000]

# expected output:10
print(x[0])
# expected output:200
print(x[-2])
print(x[4])

# Using the "loop" to print the index of the list
for indx in range(len(x)):
    print(indx, x[indx])
    
    for indx in range(0, len(x)):
        print(indx, x[indx])
        
for value in range(0, len(x)):
    print(value)

# Also can in the x to call the element in the list
for value in x:
    print(value)
    
for i in x:
    print(i)
