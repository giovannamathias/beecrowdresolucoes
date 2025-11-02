#1151 Fibonacci Fácil

ult = 1
pen = 0
aux = 0
entrada = int(input())
print(pen, ult, end='')
for x in range(entrada - 3):
    aux = pen
    pen = ult
    ult = aux + ult
    print(' '+str(ult), end='')
print(' '+str(ult+pen))
