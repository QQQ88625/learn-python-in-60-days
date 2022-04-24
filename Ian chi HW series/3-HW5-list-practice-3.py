x = [[0, 1, 2], [10, 20, 30]]

for index_1 in range(len(x)):
    for index_2 in range(len(x[index_1])):
        print(x[index_1][index_2]) 
       
for index_1 in range(len(x)):
    for value in x[index_1]:
        print(value)