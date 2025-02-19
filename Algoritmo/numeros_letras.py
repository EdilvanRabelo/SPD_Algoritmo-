# Criar um metodo para criptografar palavras em numeros e vice-versa.
# Cada letra tem um numero correspondente.
# Criar uma lista de letras e numeros.
# Solicitar ao usuario uma palavra ou numeros o usuario decide.
# Se for numeros, converter para letras.
# Se for letras, converter para numeros.
# Mostrar o resultado.
def numeros_letras():
    letras_numeros = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
    }
    numeros_letras = {v: k for k, v in letras_numeros.items()}

    while True:
        opcao = input("Digite '1' para converter letras para números ou '2' para converter números para letras: ")

        if opcao == '1':
            print("Por favor, digite uma palavra:")
            palavra = input()
            if palavra.isalpha():
                numeros_palavra = []
                for letra in palavra:
                    if letra in letras_numeros:
                        numeros_palavra.append(letras_numeros[letra])
                    else:
                        print(f"Erro: A letra '{letra}' não corresponde a um número. Por favor, tente novamente.")
                        break
                if len(numeros_palavra) == len(palavra):
                    print(f"A palavra '{palavra}' em números é: {', '.join(numeros_palavra)}")
            else:
                print("Por favor, digite uma palavra válida.")
        elif opcao == '2':
            print("Por favor, digite números separados por vírgula (valores válidos: 1 a 26): ")
            numeros = input()
            if all(x.isdigit() or x == ',' for x in numeros):
                numeros = [x for x in numeros.split(',') if x != '']
                letras_palavra = []
                for numero in numeros:
                    if 1 <= int(numero) <= 26:
                        if numero in numeros_letras:
                            letras_palavra.append(numeros_letras[numero])
                        else:
                            print(f"Erro: O número '{numero}' não corresponde a uma letra. Por favor, tente novamente.")
                            break
                    else:
                        print(f"Erro: O número '{numero}' não é válido. Por favor, digite um número entre 1 e 26.")
                        break
                if len(letras_palavra) == len(numeros):
                    print(f"Os números '{', '.join(numeros)}' em letras são: {', '.join(letras_palavra)}")
            else:
                print("Por favor, digite números válidos separados por vírgula.")
        else:
            print("Por favor, digite uma opção válida.")

        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break

numeros_letras()