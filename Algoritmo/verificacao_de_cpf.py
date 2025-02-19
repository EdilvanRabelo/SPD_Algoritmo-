# Criar um metodo que verifique se o cpf eh valido.
# Solicitar ao usuario o cpf.
# O cpf deve ter 11 digitos, somente numeros, sem pontos ou tracos.
# Verificar se o cpf eh valido.
# Se for, mostrar uma mensagem dizendo que o cpf eh valido e solicitar um novo cpf.
# Se nao for, mostrar uma mensagem dizendo que o cpf eh invalido e mostar o cpf com ponte e traço.

def verificar_cpf(cpf):
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) == 11 and cpf.isdigit():
        return True
    return False

def main():
    while True:
        cpf = input("Digite o CPF: ")
        if verificar_cpf(cpf):
            print("CPF válido!")
            print("Deseja verificar outro CPF? (s/n)")
            resposta = input().lower()
            if resposta != "s":
                break
        else:
            print("CPF inválido!")

if __name__ == "__main__":
    main()