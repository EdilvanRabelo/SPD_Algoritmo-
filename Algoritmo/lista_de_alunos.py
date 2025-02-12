# Criar um metodo que identifique o aluno de acordo com o número da lista.
# Receber uma lista de alunos e números.
# Solicitar um numero correspondente ao aluno.
# Verificar se o numero informado é valido.
# Se for, mostrar o aluno correspondente.
# Se nao for, mostrar uma mensagem dizendo que o numero informado nao eh valido e solicitar novamento o numero do aluno.

# Criando uma lista de alunos com alguns nomes pré-definidos.
alunos = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo"]

while True:
    # Solicitando ao usuário que informe um número correspondente à posição do aluno.
    # O número deve ser um inteiro entre 1 e o tamanho da lista.
    numero = int(input("Digite o número do aluno que deseja buscar (1 a 5): "))

    # Verificando se o número informado é válido.
    # O número deve estar dentro do intervalo de índices da lista.
    if 1 <= numero <= len(alunos):
        # Acessando o aluno na posição informada.
        # Subtraímos 1 do número porque a lista começa no índice 0.
        aluno = alunos[numero - 1]
        
        # Exibindo o nome do aluno correspondente.
        print(f"O aluno número {numero} da lista é: {aluno}")
        break
    else:
        # Caso o número informado seja inválido, exibe uma mensagem de erro.
        print(f"Número inválido! Por favor, digite um número entre 1 e {len(alunos)}.")