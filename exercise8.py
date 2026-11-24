def average (num):
    return sum(num) / len(num)

 # handle ZeroDivisionError

try:
    result = average([])
    print("average:",result)
except ZeroDivisionError:
    print("cannot calulate average of an empty list!")

# handle IndexError

nums= [10,20,30,40]
try:
    print(nums[99])
except IndexError:
    print("Error:List index does not exist!")

    #handle value error

try: 
    num=int("not a number")
    print(num)
except ValueError:
    print("Error : please enter a valid number!")

# bonus: safe divide function

def safe_divide(a,b):
    try:
        return a/b 
    except ZeroDivisionError:
        return "undefined"

print("10 / 2 =", safe_divide(10,2))
print("10 / 0 =", safe_divide(10,0))


