# Input the string as a list of characters
import random;
input_string = list(input("Enter the string: "))

# Delete at least 2 characters
if len(input_string) >= 2:
    rand1=random.randint(0,len(input_string)-1)
    input_string.pop(rand1)
    rand2=random.randint(0,len(input_string)-1)
    input_string.pop(rand2)
    
# Reverse the resulting string
result_string = input_string[::-1]

# Print the reversed string
print("Resulting String:", "".join(result_string))

# # Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
division_result = num1 / num2


# Print the results of arithmetic operations
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)
