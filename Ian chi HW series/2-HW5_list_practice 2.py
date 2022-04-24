# practicing for index in rang(length)
def check_one_dimension_list_version_1(data, target_value):
    for index in range(len(data)):
        if target_value == data[index]:
            return True
    return False
check_one_dimension_list_version_1([2, 3, 4, 5], 7)

check_one_dimension_list_version_1([2, 3, 4, 5], 2)


def check_one_dimension_list_version_1(data, target_value):
    for index in range(len(data)):
        if target_value == data[index]:
            return True
        else:
            return False
check_one_dimension_list_version_1([2, 3, 4, 5], 7)

# practicing for value in varible
def check_one_dimension_list_version_1(data, target_value):
     for index in data:
         print(index)


def check_one_dimension_list_version_2(data, target_value):
    for value in data:
        if target_value == value:
            return True
    return False
check_one_dimension_list_version_2([2, 3, 4, 5], 7) 

def check_one_dimension_list_version_3(data, target_value):
    if target_value in data:
        return True
    else:
        return False

check_one_dimension_list_version_3([2, 3, 4, 5], 7) 
    