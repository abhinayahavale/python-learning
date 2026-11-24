# 1. Remove duplicates using set()

nums = [4, 2, 7, 2, 4, 9, 4]
unique_nums = set(nums)
print("Original list:", nums)
print("Without duplicates:", unique_nums)
print("Number of unique numbers:", len(unique_nums))


# 2. Check whether a list has duplicates

def has_duplicates(items):
    return len(items) != len(set(items))
print("Has duplicates:", has_duplicates([4, 2, 7, 2, 4, 9, 4]))
print("Has duplicates:", has_duplicates([1, 2, 3, 4]))


# 3. Count each letter using dictionary

text = "mississippi"
counts = {}
for letter in text:
    counts[letter] = counts.get(letter, 0) + 1
print("Letter counts:", counts)


# 4. Bonus: Find the most frequent letter

most_frequent = max(counts, key=counts.get)
print("Most frequent letter:", most_frequent)
print("Frequency:", counts[most_frequent])




