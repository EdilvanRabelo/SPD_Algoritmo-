# Criar um metodo que mostre se o numero é impar de 0 a 10.
# Solicitar ao usuario um numero de 0 a 10.
# Verificar se o numero é impar.   
#  Se for, mostrar uma mensagem dizendo que o numero é impar. 
# Se nao for, mostrar uma mensagem dizendo que o numero nao é impar. 
def pedir_numero(minimo, maximo):
    while True:
        try:
            numero = int(input(f"Digite um número entre {minimo} e {maximo}: "))
            if minimo <= numero <= maximo:
                return numero
            else:
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def numero_impar_0_a_10():
    numero = pedir_numero(0, 10)

    if numero % 2 != 0:
        print(f"O número {numero} é ímpar.")
    else:
        print(f"O número {numero} não é ímpar.")

numero_impar_0_a_10()