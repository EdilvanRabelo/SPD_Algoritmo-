# Criar um algorítimo que verifique se o saldo de uma conta da para comprar um produto.
# Receber o valor do produto e o saldo da conta.
# Se o saldo for maior ou igual ao valor do produto, mostrar uma mensagem de compra realizada e saldo atual.
# sS o saldo for menor que o valor do produto, mostrar uma mensagem de saldo insuficiente saldo atual.  

def verificar_saldo():
    # Solicitar valor do produto e saldo da conta
    while True:
        try:
            valor_produto = float(input("Digite o valor do produto: R$ "))
            saldo_conta = float(input("Digite o saldo da conta: R$ "))
            break
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")

    # Verificar se o saldo é suficiente
    if saldo_conta < 0:
        print("Erro: Saldo não pode ser negativo.")
    elif saldo_conta < valor_produto:
        print("Saldo insuficiente.")
    else:
        # Calcular troco
        troco = saldo_conta - valor_produto
        print(f"Compra realizada com sucesso! Saldo atual: R$ {troco:.2f}")

verificar_saldo()