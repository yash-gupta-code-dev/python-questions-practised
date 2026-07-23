numbers = [10, 11, 12, 13, 14, 15, 16]

def sort_numbers_by_remainder(numbers):
    sorted_numbers_list = {}
    for number in numbers:
        remainder = number % 3
        if remainder not in sorted_numbers_list:
            sorted_numbers_list[remainder] = []
        sorted_numbers_list[remainder].append(number)
    return sorted_numbers_list

sorted_numbers_list = sort_numbers_by_remainder(numbers)
print(sorted_numbers_list)
