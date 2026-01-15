word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if len(word1) != len(word2):
    print("Not Anagram")
else:
    count = 0

    for ch in word1:
        if ch in word2:
            count = count + 1

    if count == len(word1):
        print("Anagram")
    else:
        print("Not Anagram")
