
# 1. Function to return even numbers from a list
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# 2. Function to count characters in a string
def char_count(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

# 3. Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 4. Function to calculate average of variable-length arguments
def average(*args):
    return sum(args) / len(args) if args else 0

# 5. Function to find common elements between two lists without using set operations
def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common


print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(char_count("hello"))
print(is_palindrome("madam"))
print(average(10, 20, 30))
