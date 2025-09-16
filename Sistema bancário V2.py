import textwrap

def menu():
    menu = """"\n
    ============ MENU ============
    Escolha a opção desejada:

        [d]\tDeposito
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Conta
        [nu]\tNovo Usuário
        [q]\tSair
      
    =>  """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        print("\nDeposito efetuado!")
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        
    else:
        print("\nOperação falhou: valor invalido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente!")
        
    elif excedeu_limite:
        print("\nLimite diário excedido, permitido no máximo R$ 500.00!")

    elif excedeu_saque:
        print("\nNúmero máximo de saque excedido")
        
    elif valor > 0:
        print("\nSaque efetuado!\n")
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saque += 1
        
    else:
        print("\nValor informado inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
     
    print ("\n============ Extrato ============")
    print("\nNão foram realizadas movimetações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print ("\n=================================")

def criar_usuario(usuarios):
    cpf = input("Informe os numeros do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nEsse usuário está cadastrado!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento= input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (Rua, número, bairro, cidade - EE): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("\nUsuário cadastrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta Criada com Sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado!")

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
    numero_saque = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
         
            valor = float(input("Digite o valor que desea sacar: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saque = numero_saque,
                limite_saque = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
    
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
            print("Opção invalida!")

main()