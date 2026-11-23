nums = [2, -1, 4, 7, 9]
target = 7
for n in nums:
      if n == target:
          break       # Stop when n is 7

      if n < 0:
          continue    # Skip negative numbers

      print(n)