#Simple calculator

#Arthmetic functions

def add(valueA, valueB):
    return valueA + valueB
def sub(valueA, valueB):
    return valueA - valueB
def mult(valueA, valueB):
    return valueA * valueB
def div(valueA, valueB):
    return valueA / valueB

print(
    "Please select an operation: -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"
    )

selectedOperation = int(input("Selec operation from 1 to 4: "))

valueA = int(input("Enter the first value: "))
valueB = int(input("Enter the second value: "))


