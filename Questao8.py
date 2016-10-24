if __name__ == '__main__':
    pass

idades = []
alturas = []

for i in range(5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("digite a altura: ")))
for i in range(5):
    print(" A idade %d e altura %.2f foi lida"%(idades[4-i],alturas[4-i]))