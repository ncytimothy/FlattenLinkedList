# Duplicating Number
### Problem Statement

# You have been given an array of `length = n`. The array contains integers from `0` to `n - 2`. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array
#
# **Example:**
# * `arr = [0, 2, 3, 1, 4, 5, 3]`
# * `output = 3` (because `3` is present twice)
#
# The expected time complexity for this problem is `O(n)` and the expected space-complexity is `O(1)`.

# O(n^2) solution
# def duplicate_number(array):
#     new_array = []
#     for digit in array:
#         if digit not in new_array:
#             new_array.append(digit)
#         else:
#             return digit

# Generalized
def duplicate_number(array):
    number_dict = dict()
    for digit in array:
        if number_dict.get(digit) is not None:
            return digit
        else:
            number_dict[digit] = 1

# Not very general purpose
def duplicate_number_sum(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    expected_sum = 0
    current_sum = 0

    for i in range(len(arr) - 1):
        expected_sum += i

    for value in arr:
        current_sum += value

    return current_sum - expected_sum

arr = [0, 2, 3, 1, 4, 5, 3]
arr1 = [0, 3, 1, 4, 5, 3]

assert 3 == duplicate_number(arr)
assert 3 == duplicate_number_sum(arr)

# assert 3 == duplicate_number_sum(arr1)
# Fails, if the problem is more generalized
# print(duplicate_number_sum(arr1))
