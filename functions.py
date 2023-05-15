def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest = numbers[0]  # Assume the first number is the largest

    for number in numbers:
        if number > largest:
            largest = number

    return largest

# Test the function
number_list = [10, 5, 20, 8, 15]
largest_number = find_largest_number(number_list)
print("The largest number is:", largest_number)
