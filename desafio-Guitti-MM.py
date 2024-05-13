menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Insira o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += (f"\n Deposito realizado de R$ {deposito:.2f}")
            print("Operação realizada")
        else:
            print("Erro, favor revisar valor do deposito OBS: Não é possivel realizar depositos negativos")

    elif opcao == "s":
        saque_h = int(input("Informe o valor a ser sacado: "))
        if saque_h < 0:
            saque = saque_h*-1
        else:
            saque = saque_h
        if saque > saldo:
            print("Saldo insuficiente")
        elif numero_saques == 3:
            print("Numeros de saques diarios já atingidos, permitido apenas 3 saques por dia")
        elif saque >= 500:
            print("Permitido apenas R$ 500,00 por saque")
        else:
            saldo -= saque
            numero_saques += +1
            extrato += f"\n Saque de R$ {saque:.2f}"


    elif opcao == "e":
        print(" EXTRATO ".center(40,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========".center(40,"="))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")