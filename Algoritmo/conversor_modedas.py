# Criar um método para converter moedas.
# Solicitar ao usuário o valor em real.
# Calcular o valor em dólar.
# Mostrar o valor em dólar .                      
def converter_moeda():
    # Solicitar ao usuário o valor em real
    valor_real = float(input("Digite o valor em real: "))

    # Cotação do dólar em relação ao real (você pode alterar essa cotação)
    cotacao_dolar = 5.20

    # Calcular o valor em dólar
    valor_dolar = valor_real / cotacao_dolar

    # Mostrar o valor em dólar
    print(f"{valor_real} reais é igual a {valor_dolar:.2f} dólares")

# Chamar o método
converter_moeda()