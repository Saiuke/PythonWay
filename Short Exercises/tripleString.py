def tripleString(string):
    result = ''
    for char in string:
        result += 3 * char
    return result

print(tripleString('O gato comeu o rato'))
print(tripleString('¿Hola que tal?'))