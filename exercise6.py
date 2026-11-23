def square(n):
    return n * n
print ("square of 5:",square(5))
print ("square of 8:",square(8))

def is_even(n):
    return n % 2 == 0
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))

def greet(name, language):
    if language == "spanish":
        return "Hola, " + name + "!"
    elif language == "french":
        return "hii, " + name + "!"
    else:
        return "Hello, " + name + "!"

print(greet("Alex", "spanish"))
print(greet("John", "french"))
print(greet("Sam", "english"))
print(greet("David", "german"))

def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average([85, 92, 78, 90, 65]))