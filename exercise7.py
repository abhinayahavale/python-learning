book = {"title": "stranger", "author": "jhon","year": 1988}
print("The book", book["title"], "was written by",book ["author"], "in", book["year"])
book["genre"] = "Adventure"
book["year"] = 1993
print("Updated book:", book)
print("Book price:", book.get("price","Not available"))
for key, value in book.items():
    print(key, ":", value)

students = [
    {"name": "Asha", "grade": 85},
    {"name": "Rahul", "grade": 92},
    {"name": "Priya", "grade": 78}
]
for student in students:
    print(student["name"], ":", student["grade"])
def average(numbers):
    return sum(numbers) / len(numbers)
grades = []

for student in students:
    grades.append(student["grade"])
print("Average grade:", average(grades))