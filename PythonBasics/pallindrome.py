word = input("Enter a word: ")

reverse = ""

for ch in word:
    reverse = ch + reverse   # build reverse word

if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
