x = [10, 20, 30, 40]
# for xxx in range(len(x))
def calculate_sum_version_1(data):
    sum = 0
    for index in range(len(data)):
        sum += data[index]
        print(sum)
        
calculate_sum_version_1(x)

# practicing return in def fuction
def calculate_sum_version_1(data):
    sum = 0
    for index in range(len(data)):
        sum += data[index]
        return sum
        print(sum)
        
calculate_sum_version_1(x)

def calculate_sum_version_1(data):
    sum = 0
    for index in range(len(data)):
        sum += data[index]
    return sum
calculate_sum_version_1(x)  

def calculate_sum_version_1(data):
    sum = 0
    for index in range(len(data)):
        sum += data[index]
    return sum
    print(sum)
calculate_sum_version_1(x) 

# for value in varible     
def calculate_sum_version_2(data):
    sum = 0 
    for value in data:
        sum += value
    return sum
calculate_sum_version_2(x) 

# average practice

def calculate_average(data):
    if len(data) == 0:
        return 0
    
    average = 0
    for value in data:
        average += value
    return average/len(data)
calculate_average(x) 


