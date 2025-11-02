#1079 Médias Ponderadas
testes = int(input())
cont = 0

while cont < testes:
    cont = cont + 1
    medias = input().split()
    media1 = float(medias[0])
    media2 = float(medias[1])
    media3 = float(medias[2])    
    media_pond = ((media1*2) + (media2*3) + (media3*5)) / 10
    print(f'{media_pond:.1f}')
