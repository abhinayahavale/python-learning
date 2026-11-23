# A function with two PARAMETERS: first_num and second_num.
# Parameters are values given to a function.
def multiply_numbers(first_num, second_num):
    # This CALCULATION multiplies the two numbers.
    # return sends the answer back to where the function was called.
    return first_num * second_num

# We call the function with 4 and 5. These are called arguments.
result = multiply_numbers(4, 5)
print(result)

# This function takes one PARAMETER called name.
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Abhinaya Havale")
say_hello("Priya")

# This function takes two PARAMETERS and does an addition calculation.
def add_numbers(first_number, second_number):
    total = first_number + second_number
    # return sends the total back.
    return total

answer = add_numbers(10, 20)
print(answer)

# We can use the returned answer in another calculation.
double_answer = answer * 2
print(double_answer)

# This function has one PARAMETER: age.
def check_age(age):
    # if / else makes a decision based on the age.
    if age >= 18:
        return "Adult"
    else:
        return "Under 18"

age_result = check_age(19)
print(age_result)

# a function with a default value

def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Abhinaya")
greet("Priya", "Good morning")