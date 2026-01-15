num = int(input("Enter a number: "))

# if-elif-else
if num > 0:
    print("Number is Positive")

    # nested if
    if num % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")

elif num < 0:
    print("Number is Negative")

else:
    print("Number is Zero")

# for loop
print("\nPrinting numbers from 1 to", abs(num))
for i in range(1, abs(num) + 1):
    print(i)
