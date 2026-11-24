s = "programming"
print("first 4 char",s[:4])
print("last 3 char:",s[-3:])
print("without first and last:",s[1:-1])
print ("reversed string:",s[::-1])

word= "racecar"

if word == word[::-1]:
    print("Is palindrome:", True)
else:
    print("Is palindrome:", False)

sentence = "learning python is fun"
print("stripped:", sentence.strip())
print("uppercase:",sentence.upper())

words = sentence.split()
print("word list:", words)
print ("number of words:", len(words))

text= "hello world foo"
reversed_words = " ".join(text.split()[::-1])
print("reversed word order:", reversed_words)
