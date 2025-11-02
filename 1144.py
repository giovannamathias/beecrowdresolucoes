#1144 Sequência Lógica
entrada = int(input())
x = 1
for i in range(1, entrada + 1):
    print(f'{x} {x**2} {x**3}')
    print(f'{x} {(x**2) + 1} {(x**3) +1 }')
    x = x + 1
