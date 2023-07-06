# Task 2

# To filter a list of integers to get only the even numbers using the filter() function and a lambda function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
