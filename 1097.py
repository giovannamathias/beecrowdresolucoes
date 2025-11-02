#1097 Sequência IJ 3
J = 7
I = 1
for I in range (1, 10, 2):
    for u in range(3):
        print(f'I={I} J={J}')
        J = J - 1
    J = I + 8
