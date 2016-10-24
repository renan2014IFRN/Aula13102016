if __name__ == '__main__':
    pass

codigos = [0,0,0,0,0]

for i in range(250):
    print("Os codigos de erros são:")
    print("1 - Necessita da esfera")
    print("2 - Necessita da limpeza")
    print("3 - Necessita da troca do cabo ou conector")
    print("4 - Quebrado ou inultilizado")
    print("Digite 0 para sair")

    codigoErro = int(input("Digite o codigo do erro identificado: "))
    if codigoErro!=0:
        codigos[codigoErro]=+1

    else:
        print("%d - Necessita(m) da esfera"%codigos[1])
        print("%d - Necessita(m) da limpeza"%codigos[2])
        print("%d - Necessita(m) da troca do cabo ou conector"%codigos[3])
        print("%d - Quebrado(s) ou inultilizado(s)"%codigos[4])
        break