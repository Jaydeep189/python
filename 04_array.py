main_array = []

main_array_length = int(input("Enter the length of the main array"))

for n in range(main_array_length):
    main_array.append(int(input("Enter an element")))

program_flag = True

def display_array(array):
    for i in array:
        print(i)

def find_length():
    print(len(main_array))

def insert_element(element):
    main_array.append(element)
    display_array(main_array)

def delte_element(element):
    is_present = False
    for n in main_array:
        if n == element:
            is_present = True
            main_array.remove(element)
    if is_present:
        display_array(main_array)
    else:
        print("\nElement not present")

def search_element(element):
    is_present = False
    for n in main_array:
        if n == element:
            is_present = True
            print("The element is at index", main_array.index(n))
    if is_present:
        display_array(main_array)
    else:
        print("\nElement not present")    

def update_element(element, value):
    is_present = False
    for n in main_array:
        if n == element:
            is_present = True
            main_array[main_array.index(n)] = value
    if is_present:
        display_array(main_array)
    else:
        print("\nElement not present")

def concate(array):
    concated_array = main_array + array
    display_array(concated_array)

while(program_flag):
    choice = int(input(
        "1. Find Length\n2. Insert Element\n3. Delete Element\n4. Search Element\n5. Update Element\n6. Concate\n-1. Exit\n"
    ))
    if choice == -1:
        program_flag = False
    elif choice == 1:
        find_length()
    elif choice == 2:
        value_2 = int(input("Enter a new Element"))
        insert_element(value_2)
    elif choice == 3:
        value_3 = int(input("Enter a element to delete"))
        delte_element(value_3)
    elif choice == 4:
        value_4 = int(input("Search an element in the list: "))
        search_element(value_4)
    elif choice == 5:
        value_5 = int(input("Enter the value you want to update: "))
        value_5_new = int(input("Enter the new value to replace"))
        update_element(value_5, value_5_new)
    elif choice == 6:
        value_6_len = int(input("Enter the length of the new array: "))
        new_array = []
        for i in range(value_6_len):
            new_array.append(int(input("Enter an element")))
        concate(new_array)