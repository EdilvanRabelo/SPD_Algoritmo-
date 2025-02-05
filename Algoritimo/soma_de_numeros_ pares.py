# criar metodo para somar numeros pares.
# receber uma lista de numeros
# verificar se o numero e par ou impar
# se for par, somar.
# Se for impar, nao somar
# mostrar os numeros pares e o resultado da soma.

def somar_numeros_pares(numeros): 
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma