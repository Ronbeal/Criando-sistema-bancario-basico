menu = """ =========== MENU ===========
      
      Escolha a opção desejada:

      [d] Deposito
      [s] Sacar
      [e] Extrato
      [q] Sair
      
      -> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            print("\n\nDeposito efetuado!\n\n")
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou: valor invalido")

    elif opcao == "s":
        valor = float(input("Digite o valor que desea sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")
        
        elif excedeu_limite:
            print("Limite diário excedido, permitido no máximo R$ 500.00!")

        elif excedeu_saque:
            print("Número máximo de saque excedido")
        
        elif valor > 0:
            print("\n\nSaque efetuado!\n\n")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Valor informado inválido!")

    elif opcao == "e":
        print ("\n============ Extrato ============")
        print("Não foram realizadas movimetações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print ("\n=================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
