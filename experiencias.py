#Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
#organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
#quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
#laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
#informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
#utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
#valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
#inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
#de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
#cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
#percentual deve ser apresentado com dois dígitos após o ponto.

coelho=0
s=0
r=0
totc=0

t=int(input("Informe a quantidade de testes realizados: "))
for c in range(t):
    qtdc=int(input("Informe a quantidade de cobaias utilizadas: "))
    tpc=str(input("Informe o tipo de cobaia: ")).strip().upper()[0]
    totc+=qtdc
    if tpc=='C':
        coelho=coelho + qtdc
    elif tpc=='R':
        r=r+qtdc
    else:
        s=s+qtdc

perc=((coelho/totc)*100)
perr=((r/totc)*100)
pers=((s/totc)*100)


print(f"A quantidade total de cobaias foram {totc}")
print(f"O total de coelhos foi {coelho}")
print(f"O total de sapos foi {s}")
print(f"O total de ratos foi {r}")
print(f"O percentual de coelhos foi {perc:.2f}")
print(f"O percentual de ratos foi {perr:.2f}")
print(f"O percentual de sapos foi {pers:.2f}")