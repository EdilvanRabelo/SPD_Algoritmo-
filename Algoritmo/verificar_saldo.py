# criar um algoritimo que verifique se o saldo de uma conta da para comprar um produto
#receber o valor do produto e o saldo da conta.
# se o saldo for maior ou igual ao valor do produto, mostrar uma mensagem de compra realizada.
# se o saldo for menor que o valor do produto, mostrar uma mensagem de saldo insuficiente.  

# Solicita ao usuário o valor do produto
produto = float(input("Digite o valor do produto: "))

# Solicita ao usuário o saldo da conta
saldo = float(input("Digite o saldo da conta: "))

# Verifica se o saldo é suficiente para comprar o produto   
if saldo >= produto:
    print("Compra realizada com sucesso!")
    print("Troco: R$", saldo - produto)
    saldo_atual = saldo - produto
    if saldo_atual > 0:
        print("Seu saldo atual é positivo: R$", saldo_atual)
    elif saldo_atual < 0:
        print("Seu saldo atual é negativo: R$", saldo_atual)
    else:
        print("Seu saldo atual é zero.")
else:
    print("Saldo insuficiente.")
    saldo_atual = saldo - produto
    if saldo_atual > 0:
        print("Seu saldo atual é positivo: R$", saldo_atual)
    elif saldo_atual < 0:
        print("Seu saldo atual é negativo: R$", saldo_atual)
    else:
        print("Seu saldo atual é zero.")