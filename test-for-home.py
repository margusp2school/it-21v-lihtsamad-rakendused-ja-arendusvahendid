def add(a, b): 
    return a + b 

# how can I add 4 numbers (1, 2, 3, 4) with only function add? 
# hint: return value of f(f(a, b), f(c, d))
sum_of_numbers = ...

# print out biggest number in 2 arrays?
my_number1 = int(input("Please enter nr 1:"))
my_number2 = int(input("Please enter nr 2:"))
my_array1 = [12, 55, 23, my_number1]
my_array2 = [99, 33, my_number2, 5]

def print_out_biggest_number(array_of_numbers_as_argument):
    # hint use temporary variable
    # biggest_number_temporary_variable = 0
    # for number in array_of_numbers_as_argument:
    #   if number > biggest_number_temporary_variable:
    #     assign number value to temporary variable