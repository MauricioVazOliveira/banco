menu = """

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("valor que deseja depositar"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$:{valor:.2f}\n"

        else:
            print("opção inválida, adicione um valor maior que 0")


    elif opcao == "s":
        valor = float(input("Digite o valor para saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou, sem saldo suficiente")

        elif excedeu_limite:
            print("limite de saque excedido")

        elif excedeu_saque:
            print("limite de saque excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Retirada: R$:{valor:.2f}\n"
            numero_saques += 1

        else:
            print("valor invalido")

    elif opcao == "e":
        print("===================Extrato=====================")

        print("nao foi realizado nenhuma operação" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")


        print("===================Extrato=====================")

    elif opcao == "q":
        break

    else:
        print("opção invalida, selecione uma das opções abaixo")