#1096 Sequência IJ 2
I = 1
J = 7
for v in range(5):
    J = 7
    I = I
    for u in range(3):
        print(f'I={I} J={J}')
        J  = J - 1
    I = I + 2
