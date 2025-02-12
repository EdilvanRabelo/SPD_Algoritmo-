# Problema: Conversão de Números inteiros para Romanos.
# Você precisa implementar uma função que converta um número inteiro em seu equivalente Romano.
# Receber um numero inteiro. 
# O número deve estar entre 1 e 3999.
# Retornar o número romano correspondente.

# Define a função int_to_roman que recebe um número arábico (num) como argumento.
def int_to_roman(num):
    # Lista de valores arábicos em ordem decrescente.
    val = [
        1000, 900, 500, 400,100, 90, 50, 40, 10, 9, 5, 4,1                    
    ]

    # Lista de símbolos romanos correspondentes aos valores acima.
    syms = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"                    
    ]

    # Variável para armazenar o número romano final.
    roman_num = ''

    # Índice para percorrer as listas val e syms.
    # Começa em 0 para acessar o maior valor primeiro.
    i = 0

    # Loop while que continua enquanto o número arábico (num) for maior que 0.
    while num > 0:
        # Verifica quantas vezes o valor atual (val[i]) cabe no número arábico
        # Por exemplo, se num = 1987 e val[i] = 1000, então 1987 // 1000 = 1
        for _ in range(num // val[i]):
            # Adiciona o símbolo romano correspondente ao resultado
            roman_num += syms[i]
            # Subtrai o valor arábico do número original
            num -= val[i]

        # Incrementa o índice para passar para o próximo valor e símbolo
        i += 1

    # Retorna o número romano construído
    return roman_num

# Solicita que o usuário digite um número
try:
    # Usa a função input() para receber a entrada do usuário
    # int() converte a entrada para um número inteiro
    numero = int(input("Digite um número entre 1 e 3999: "))

    # Verifica se o número está dentro do intervalo válido (1 a 3999)
    if 1 <= numero <= 3999:
        # Se estiver dentro do intervalo, chama a função int_to_roman para converter o número e exibe o resultado.
        print(f"O número {numero} em algarismos romanos é: {int_to_roman(numero)}")
    else:
        # Se o número estiver fora do intervalo, exibe uma mensagem de erro.
        print("Por favor, digite um número entre 1 e 3999.")
except ValueError:
    # Captura erros caso o usuário digite algo que não seja um número inteiro.
    # Por exemplo, se o usuário digitar "abc" ou "12.5"
    print("Entrada inválida. Por favor, digite um número inteiro.")