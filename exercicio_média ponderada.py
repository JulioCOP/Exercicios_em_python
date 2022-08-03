#Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada
#caso de teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a
#média ponderada, sendoque o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro
#valor tem peso 5. Vale lembrar que a média ponderada é a soma de todos os valores multiplicados
#pelo seu respectivo peso, dividida pela soma dos pesos.
media=0
v= int(input("Informe quantos números você deseja: "))
for c in range(v):
    valor1=float(input(" "))
    valor2=float(input(" "))
    valor3=float(input(" "))
    media=((valor1*2) + (valor2*3) + (valor3*5))/ (2+3+5)
    print(f"A média ponderada é {media:.2f}")