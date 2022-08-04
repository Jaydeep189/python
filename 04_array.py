if __name__ == "__main__":
    program_flag = True
    no_of_arrays = int(input("Enter the no of arrays: "))
    dic_of_arrays = {}
    def input_into_array():
        dic_array = []
        n = int(input("no of element in array : "))
        for i in range(1, n+1):
            ele = int(input())
            dic_array.append(ele)
        return dic_array
    for i in range(1, no_of_arrays+1):
        dic_of_arrays[i] = input_into_array();
    while program_flag:
        choice = int(input(
            " "
        ))

def add_into_array(dic_key, value):
    dic_of_arrays[dic_key].append(value)
    print(dic_of_arrays[dic_key])

def delete_from_array(dic_key, element):
    try:
        dic_of_arrays[dic_key].remove(element)
    except:
        print("Element is not present in the array")  

def update_in_array(dic_key, element):
    try:
        for i in dic_of_arrays[dic_key]:
            if i == element:
                index = dic_of_arrays[dic_key].index(i)
                value = int(input("Enter a new value: "));
                dic_of_arrays[dic_key][index] = value
    except:
        print("Element is not present in the array") 

def search_in_array(dic_key, value):
    flag = 0
    for i in dic_of_arrays[dic_key]:
        if i == value:
            print("Element is present at position", dic_of_arrays[dic_key].index(i))     
            flag = 1
    if flag == 0:
        print("Element is not present in the array") 

def length_of_arrays():
    for length in dic_of_arrays:
        print("the length of the array " + str(length) + " is", len(dic_of_arrays[length]))

def concate_list(dic_key_1, dic_key_2):
    print("concated list \n", dic_of_arrays[dic_key_1] + dic_of_arrays[dic_key_2])