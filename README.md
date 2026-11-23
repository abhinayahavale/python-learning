# Python Learning Notes

This folder contains my beginner Python practice programs.

## Run a Python file

Open Terminal in this folder and run a file with:

```bash
python3 main.py
```

Replace `main.py` with the file you want to run, for example `list.py` or `function.py`.

## 1. Variables

A variable stores information so it can be used later.

```python
name = "Abhinaya"
age = 19
hobby = "Dancing"
```

- Text uses quotation marks: `"Dancing"`
- Whole numbers do not use quotation marks: `19`

## 2. Printing output

`print()` shows information on the screen.

```python
print(name)
print("My age is", age)
```

## 3. F-strings

An f-string puts variable values inside text.

```python
print(f"My name is {name} and I am {age} years old.")
```

Put `f` before the quotation mark. Put variable names inside `{}`.

## 4. Calculations

Python can do mathematics with numbers stored in variables.

```python
birth_year = 2026 - age
next_year_age = age + 1

print(birth_year)
print(next_year_age)
```

Using `age` is better than writing the number again. If `age` changes, the calculations update automatically.

## 5. User input

`input()` asks the user to type an answer.

```python
favourite_food = input("What is your favourite food? ")
print(f"{favourite_food} sounds delicious!")
```

## 6. If and else

`if` lets Python make a decision.

```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")
```

`>=` means “greater than or equal to”. The indented lines belong to the `if` or `else` block.

## 7. Lists

A list stores several related items in one variable. Lists use square brackets `[]`.

```python
hobbies = ["dancing", "reading", "listening to music"]
```

### List positions

Python counts list positions starting at `0`.

```python
print(hobbies[0])  # first item: dancing
print(hobbies[1])  # second item: reading
```

### Add and remove list items

```python
hobbies.append("cooking")
hobbies.remove("reading")
```

`append()` adds an item at the end. `remove()` removes a matching item.

### Loop through a list

A `for` loop repeats code once for each item.

```python
for hobby in hobbies:
    print(f"I enjoy {hobby}.")
```

### Count list items

```python
print(len(hobbies))
```

`len()` counts how many items are in a list.

## 8. Dictionaries

A dictionary stores related information as `key: value` pairs. Dictionaries use curly brackets `{}`.

```python
person = {
    "name": "Abhinaya",
    "age": 19,
    "hobby": "Dancing"
}
```

### Read a dictionary value

```python
print(person["name"])
print(person["age"])
```

The key inside `[]` must match exactly.

### Add, update, and delete dictionary values

```python
person["city"] = "Mumbai"  # add
person["age"] = 20          # update
del person["hobby"]          # delete
```

After deleting a key, do not use `person["hobby"]`, because it no longer exists.

## 9. Functions

A function is a named, reusable block of code. Define it with `def`, then call it using its name and parentheses.

```python
def say_hello():
    print("Hello!")

say_hello()
```

### Function parameters

Parameters let a function receive information.

```python
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Abhinaya")
say_hello("Priya")
```

### Return values

`return` sends a result back from a function so it can be stored or used later.

```python
def add_numbers(first_number, second_number):
    total = first_number + second_number
    return total

answer = add_numbers(10, 20)
print(answer)  # 30
```

## Files in this folder

- `main.py` — variables, input, calculations, and if/else
- `list.py` — lists, loops, add/remove, and `len()`
- `dictionary.py` — dictionaries
- `function.py` — functions, parameters, and return values

## Style tips

Use spaces around `=` and after commas:

```python
age = 19
print("Hello, world!")
```

Python reads code from top to bottom. Create a variable before using it.
