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


runAgain = 'y'


def calculator():
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
    )

    selectedOperation = int(input("Selec operation from 1 to 4: "))

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
    else:
        print(
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
            "INVALID INPUT\n"
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        )

    print("\n\nDo you wish do run another operation?")
    runAgain = input("Type Y for yes and N for no: ")
    if runAgain == 'y':
        calculator()
    else:
        pass