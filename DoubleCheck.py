num = int(input("Enter number to check: "))


if num > 50:
    print("Number is greater than 50")
    if num % 2 == 0:
        print("Number is also an even number")
    else:
        print("Number is also an odd number")
else: 
    print("Number is less than 50")