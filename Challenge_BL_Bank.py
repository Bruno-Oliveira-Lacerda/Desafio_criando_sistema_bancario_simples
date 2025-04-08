menu="""
---------- MENU ----------

Selecione a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

--------------------------

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Insira o valor que deseja depositar: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
           
            print("Falha na operação! Por favor tente novamente \n")

    elif opcao == "2":

      valor = float (input("Informe o valor que deseja sacar: \n"))

      excedeu_limite = valor > limite
      excedeu_saldo = valor > saldo
      excedeu_saque =  numero_saque >= LIMITE_SAQUE

      if excedeu_limite:
          
          print("Falha na operação! Limite para saque excedido.")
     
      elif  excedeu_saldo:
          
          print("Falha na operação! Saldo insuficiente.")

      elif excedeu_saque:
          
          print("Falha na operação! Limite de saques excedido")
      
      elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saque += 1


      else:
          print("Falha na operação! O valor digitado é inválido.\n")

    elif opcao == "3":

        print("---------- EXTRATO ----------\n\n")
        print("Não foram realizadas movimentações nessa conta\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}\n")
        print("----------------------------\n")

    elif  opcao == "4":

        break

    else: 
        print("Falha na operação! Por favor selecione novamente a opção desejada\n")
