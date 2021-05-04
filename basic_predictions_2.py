def counting_down(number):
    number_array = []
    for x in range(number, 0, -1):
        number_array.append(x)
    number_array.append(0)
    return number_array

# number = int(input('Insert the number to count down: '))
# print(counting_down(number))

# Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(list):
    print(list[0])
    return list[1]

# print(print_and_return([1,2]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    return list[0] + len(list)

# print(first_plus_length([1,2,3,4,5]))

# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for x in list:
        if (x > list[1]):
            new_list.append(x)

    print(f"THIS IS THE LENGTH: {len(new_list)}")
    return new_list

# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([3]))


# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    new_array = []
    while len(new_array) <= size:
        new_array.append(value)
    return new_array

print(length_and_value(4,7))
print(length_and_value(6,2))

def length_and_value2(size, value):
    new_array = []
    for i in range(size + 1):
        new_array.append(value)
    return new_array

print(length_and_value2(4,8))
print(length_and_value2(6,3))