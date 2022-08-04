string = input("Enter a string: ")

print("The length of the string is", len(string))

print("String converted into uppercase: ", string.upper())

print("String converted into lowercase: ", string.lower())

not_rendundant_string = "".join(set(string))

for i in not_rendundant_string:
    print("The no of times " + i + " occured = ", string.count(i))

