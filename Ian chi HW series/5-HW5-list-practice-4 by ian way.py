x = [10, 20, 30, 40, 50, 60]
def calculate_sum_version_1(data):
    sum = 0
    for index in range(len(data)):
        sum += data[index]
    return sum
 


def calculate_sum_version_2(data):
    sum = 0 
    for value in data:
        sum += value
    return sum


def calculate_average(data):
    if len(data) == 0:
        return 0
    
    average = 0
    for value in data:
        average += value
    return average/len(data)
   

calculate_sum_version_1(x) 
calculate_sum_version_2(x) 
calculate_average(x) 