if __name__ == '__main__':
    pass

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro","Novembro","Dezembro"]
soma = 0
nmeses = 3
for i in range(nmeses):
    temperaturas.append(float(input("Digite a temperatura de %s: "%(meses[i]))))
    soma=+ temperaturas[i]

media = soma/nmeses
print("A media anual é %f")
'''
incompleto
'''

for i in range(nmeses):
    if media<temperaturas[i]:
        print("A temperatura %f de %s foi maior que a media anual"%(temperaturas[i],meses[i]))