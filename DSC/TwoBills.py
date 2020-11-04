vueltas = []
caja = [2, 5, 10, 20, 50, 100]
while True:
    v = input("")
    c, p = v.split(" ")
    c = int(c)
    p = int(p)
    if( c == 0 and p == 0):
        break
    r = p - c
    vueltas.append(r)