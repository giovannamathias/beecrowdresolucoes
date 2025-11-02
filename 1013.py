#1013 O maior 
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maiorAB = (a + b + abs(a - b))/2
maiorABC = (maiorAB + c + abs(maiorAB - c)) / 2
print(f'{maiorABC:.0f} eh o maior')
