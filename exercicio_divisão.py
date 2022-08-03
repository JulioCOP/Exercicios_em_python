casos=int(input("Quantos casos serão digitados: "))

for c in range(casos):
    n=float(input("Informe o numerador: "))
    d= float(input("Informe o divisor: "))

    if d==0:
        print("Divisão IMPOSSÍVEL")

    elif n==0:
        divi=0
        print(f"O resultado da divisão é 0")
    else:
        if d!=0 or n!=0:
            div=n/d
            print(f"DIVISÃO É IGUAL A {div}")

print("FIM")