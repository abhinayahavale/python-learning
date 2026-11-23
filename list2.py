fruits=["apple","banana","cherry"]
print(fruits[0])
print(fruits[-1])
print(len(fruits))
fruits[0]="avocado"
fruits.append("date")
fruits.remove("banana")
if "apple" in fruits:
    print("have apples")
for fruit in fruits:
    print(f"I Like {fruit}")
