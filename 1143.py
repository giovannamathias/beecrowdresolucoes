#1143 Quadrado e Cubo
entrada = int(input())
x = 1
for i in range(1, entrada + 1):
    print(f'{x} {x**2} {x**3}')
    x = x + 1
