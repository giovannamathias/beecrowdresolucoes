#1017 Gasto de Combustível
tempo = int(input())
vel_media = int(input())
distancia = tempo * vel_media
gasto_combus = distancia/12 
print(f'{gasto_combus:.3f}')
