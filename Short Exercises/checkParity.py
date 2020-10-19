def checkParity(n):
    if n % 2 == 0:
        result = "The number " + str(n) + " is pair"
    else:
        result = "The number " + str(n) + " is odd, as you are."
    print(result)

print("Check the parity of a given integer:")
number = input("Type the number to be evaluated: ")

if number.isnumeric() == True:
    number = int(number)
    checkParity(number)
else:
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
