# Criar um método para calcular a lei de ohm, com qualquer uma das 3 opções.
# Solicitar para informar os valores que ele tem  tensão(V), resistência(R) ou corrente(I).
# De acordo com quais os valores foram informados, Calcular a lei de ohm.
# Mostrar o resultado. e sua grandeza elétrica.

def calcular_lei_de_ohm():
    while True:
        # Solicitar qual grandeza calcular
        eletrica = input("\nQual grandeza deseja calcular? (V para Tensão, R para Resistência, I para Corrente, ou 'S' para sair): ").strip().upper()

        # Condição de saída do loop
        if eletrica == "S":
            print("Encerrando o programa...")
            break

        try:
            # Cálculo da tensão (V = I * R)
            if eletrica == "V":
                corrente = float(input("Digite a corrente (A): "))
                resistencia = float(input("Digite a resistência (Ω): "))
                if corrente < 0 or resistencia < 0:
                    print("Erro: Valores não podem ser negativos!")
                    continue
                tensao = corrente * resistencia
                print(f"\nTensão calculada: {tensao:.2f} V")

            # Cálculo da resistência (R = V / I)
            elif eletrica == "R":
                tensao = float(input("Digite a tensão (V): "))
                corrente = float(input("Digite a corrente (A): "))
                if tensao < 0 or corrente <= 0:
                    print("Erro: Tensão deve ser positiva e corrente não pode ser zero ou negativa!")
                    continue
                resistencia = tensao / corrente
                print(f"\nResistência calculada: {resistencia:.2f} Ω")

            # Cálculo da corrente (I = V / R)
            elif eletrica == "I":
                tensao = float(input("Digite a tensão (V): "))
                resistencia = float(input("Digite a resistência (Ω): "))
                if tensao < 0 or resistencia <= 0:
                    print("Erro: Tensão deve ser positiva e resistência não pode ser zero ou negativa!")
                    continue
                corrente = tensao / resistencia
                print(f"\nCorrente calculada: {corrente:.2f} A")

            else:
                print("Opção inválida! Escolha V, R ou I.")

        except ValueError:
            print("Erro: Digite apenas números válidos!")
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero!")

# Chamar a função
calcular_lei_de_ohm()
