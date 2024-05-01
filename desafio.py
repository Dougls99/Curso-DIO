import textwrap

def menu():
    menu = """\n
    =============== Sistema Bancario ===============
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [lc] \tLista contas
    [nu] \tNovo Usuário
    [q] \tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor: .2f}\n"
        print("\n ==== Depósito Realizado com Sucesso! ====")

    else:
        print("n@@@  Operação Falhou! O valor informado é invalido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação Falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@  Operação Falhou! O valor de saque excedeu  o limmite. @@@")

    elif excedeu_saques:
        print("\n@@@  Operação Falhou! Número de saques excedido. @@@")

    elif valor > 0:
        saldo  -= valor
        extrato += f"Saque: \t\tR$ {valor: .2f}\n"
        numeros_saques += 1
        print("\n ==== Saque Realizado com Sucesso! ====")

    else:
        print("\n@@@  Operação Falhou! valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *,  extrato):
    print("============ Extrato =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo: .2f}")
    print("==================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF")
        return

    nome = input("Informe seu nome Completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nº, bairro, cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=============== Usuário Criado com Sucesso ===============")

def  filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for  usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[o] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=============== Conta Criada Com Sucesso ===============")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrando, criação de conta encerrada! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"


    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do déposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do Saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione a opção desejada!")

main()