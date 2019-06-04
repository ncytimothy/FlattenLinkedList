# Add-One

### Problem Statement

## You are given a non-negative number in the form of list elements. For example, the number `123` would be provided as `arr = [1, 2, 3]`. Add one to the number and return the output in the form of a new list.

# **Example 1:**
# * `input = [1, 2, 3]`
# * `output = [1, 2, 4]`
#
# **Example 2:**
# * `input = [9, 9, 9]`
# * `output = [1, 0, 0, 0]`
#
# **Challenge:**
#
# One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have `input = [1, 2, 3]`, you could solve this problem by creating the number `123` and then separating the digits of the output number `124`.
#
# But can you solve it in some other way?

def add_one(array):
    number_str = ""
    for digit in array:
        number_str += str(digit)
    number = int(number_str) + 1
    return [int(digit) for digit in str(number)]

def add_one_new(array):
    return_array = array
    if array[len(array) - 1] is not 9:
        return_array[len(array) - 1] = return_array[len(array) - 1] + 1
        return return_array
    else:
        for (index, digit) in enumerate(return_array):
            return_array[index] = 0
        return_array.insert(0, 1)
        return return_array

# --------------------------------------------------------------------------
# First test case
input = [1, 2, 3]
input2 = [9, 9, 9]

# print(add_one(input))
# print(add_one(input2))

# print(add_one_new(input))
# print(add_one_new(input2))

# assert add_one(input) == [1, 2, 4]
# assert add_one(input2) == [1, 0, 0 ,0]

# --------------------------------------------------------------------------
# Test Function for add_one
# def test_function(test_case):
#     arr = test_case[0]
#     solution = test_case[1]
#
#     output = add_one(arr)
#     print(output)
#     for index, element in enumerate(output):
#         if element != solution[index]:
#             print("Fail")
#             return
#     print("Pass")
#
# arr = [0]
# solution = [1]
# test_case = [arr, solution]
# test_function(test_case)
#
# arr = [1, 2, 3]
# solution = [1, 2, 4]
# test_case = [arr, solution]
# test_function(test_case)

# --------------------------------------------------------------------------
# Test Function for add_one_new
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one_new(arr)
    print(output)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)
