# Pratique-Projeto-1

* Para que o sistema permita executar o script, você precisa garantir que o arquivo seja executável. Para isso é preciso usar o comando 'chmod +x calculadora.sh', onde 'x' é o atributo que torna o arquivo executável.
* No PowerShell se estiver no mesmo diretório, basta usar './' antes do nome do arquivo, no meu caso: ./calculadora.sh
* O código Python já está todo comentado:
while True:
    # Solicita ao usuário que insira dois números e converte para float para permitir números decimais
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Apresenta as opções de operação disponíveis para o usuário
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Obtém a opção escolhida pelo usuário e converte para inteiro
    opcao = int(input("Digite o número da operação: "))

    # Estrutura condicional para realizar a operação escolhida
    if opcao == 1:
        # Realiza a soma e exibe o resultado
        resultado = num1 + num2
        print("Resultado da soma:", resultado)
    elif opcao == 2:
        # Realiza a subtração e exibe o resultado
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)
    elif opcao == 3:
        # Realiza a multiplicação e exibe o resultado
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)
    elif opcao == 4:
        # Verifica se o divisor é zero para evitar erro de divisão por zero
        if num2 == 0:
            print("Divisão por zero não é permitida.")
        else:
            # Realiza a divisão e exibe o resultado
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)
    elif opcao == 5:
        # Interrompe o loop quando o usuário escolhe sair
        print("Você optou por sair")
        break
    else:
        # Exibe uma mensagem de erro para opções inválidas
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
