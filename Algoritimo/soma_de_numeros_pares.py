# criar metodo para somar numeros pares.
# receber uma lista de numeros.
# verificar se o numero e par ou impar.
# se for par, somar.
# mostrar os numeros pares e o resultado da soma.

def somar_numeros_pares():
   # Solicita entrada do usuário e cria lista de números
   numeros = input("Digite vários números separados por espaço: ")
   lista_numeros = [int(num) for num in numeros.split()]
   
   # Inicializa variáveis
   soma = 0
   numeros_pares = []
   
   # Verifica cada número
   for numero in lista_numeros:
       if numero % 2 == 0:  # Se for par
           soma += numero
           numeros_pares.append(numero)
   
   # Mostra resultados
   print(f"\nNúmeros pares encontrados: {numeros_pares}")
   print(f"Soma dos números pares: {soma}")

# Executa o programa
try:
   somar_numeros_pares()
except ValueError:
   print("Por favor, digite apenas números válidos separados por espaço")