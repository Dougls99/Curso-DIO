menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Informe o valor do déposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
            
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opção == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print("Operação falhou! Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximmo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numeros_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opção == "e":
        print("=========Extrato=========")
        print("=========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=========================")
        print("=========================")

    elif opção == "q":
        break

else:
    print("Operação invalida, por favor selecione a opção desejada!")