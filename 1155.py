#1155 Sequência S
S = 0
for i in range(1, 100 + 1):
    S = 1/i + S
print(f'{S:.2f}')   
