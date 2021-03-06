# Simple calculator

# Arthmetic functions

def add(valueA, valueB):
    return valueA + valueB

def sub(valueA, valueB):
    return valueA - valueB

def mult(valueA, valueB):
    return valueA * valueB

def div(valueA, valueB):
    return valueA / valueB

def pow(valueA, valueB):
    return valueA ** valueB

# Calculator function

def calculator():
    # Header
    print(
        "\n"
        "···········································································\n"
        "································CALCULATOR·································\n"
        "···········································································\n"
        "·································By Saiuke·································\n"
        "\n"
        "\n"
        "Please select an operation:\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n"
        "5. Power\n"
    )
    # Error message
    invalidInput = "\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n"

    selectedOperation = input("Selec operation from 1 to 5: ")

    if selectedOperation.isnumeric and int(selectedOperation) <= 5:

        selectedOperation = int(selectedOperation) #Convert the input to integer

        valueA = int(input("Enter the first value: "))
        valueB = int(input("Enter the second value: "))

        if selectedOperation == 1:
            print(valueA, " + ", valueB, " = ", add(valueA, valueB))
        elif selectedOperation == 2:
            print(valueA, " - ", valueB, " = ", sub(valueA, valueB))
        elif selectedOperation == 3:
            print(valueA, " * ", valueB, " = ", mult(valueA, valueB))
        elif selectedOperation == 4:
            print(valueA, " / ", valueB, " = ", div(valueA, valueB))
        elif selectedOperation == 5:
            print(valueA, " ** ", valueB, " = ", pow(valueA, valueB))
        else:
            print(invalidInput)

        print("\n\nDo you wish do run another operation?")
        runAgain = input("Type Y for yes and N for no: ")
        if runAgain == 'y' or runAgain == 'Y':
            calculator()
        else:
            pass
    else:
        print(invalidInput)

#Run the program, duh!
calculator()
