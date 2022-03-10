import numbers


sum = 0
while(True):
    userInput = input("Enter the price or 'q' to quit! \n")
    if (userInput != 'q'):
        sum = sum + int(userInput)
        print(f"Your bill so far: {sum}")
    else:
        print(f"Your bill is: {sum}. Thanks!!")
        break