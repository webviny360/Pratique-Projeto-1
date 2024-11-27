# -*- coding: utf-8 -*-
"""Exercício Módulo I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FookY4OTGK1mCXjtRPYHjsUAPlYLLnUc

###Que tal praticar?
Agora, você fará a primeira parte do seu primeiro projeto! Como disse o professor Rodrigo, não há uma forma fixa: o importante é que seu código siga uma sequência lógica e tenha, ao menos, os critérios abaixo, ok?

Passo a passo:

* Utilize o comando 'input' para receber ao menos 2 números de entrada do usuário;

* Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);

* Implemente ao menos 4 operações matemáticas em seu código;

* Adicione um laço de repetição ou uma condicional. Por exemplo: você pode permitir que o usuário escolha qual operação realizar ou criar um loop que permita ao usuário realizar várias operações consecutivas;

* Utilize o comando 'print' para exibir o resultado da operação matemática.
"""

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