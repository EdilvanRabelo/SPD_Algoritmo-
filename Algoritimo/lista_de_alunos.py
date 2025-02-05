# Problema identificar a quem é o aluno de acordo com o número da lista.

# 1. Criando uma lista de alunos com alguns nomes pré-definidos.
alunos = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo"]

# 2. Solicitando ao usuário que informe um número correspondente à posição do aluno.
# O número deve ser um inteiro entre 1 e o tamanho da lista.
numero = int(input("Digite o número do aluno que deseja buscar (1 a 5): "))

# 3. Verificando se o número informado é válido.
# O número deve estar dentro do intervalo de índices da lista.
if 1 <= numero <= len(alunos):
    # 4. Acessando o aluno na posição informada.
    # Subtraímos 1 do número porque a lista começa no índice 0.
    aluno = alunos[numero - 1]
    
    # 5. Exibindo o nome do aluno correspondente.
    print(f"O aluno número {numero} da lista é: {aluno}")
else:
    # 6. Caso o número informado seja inválido, exibe uma mensagem de erro.
    print(f"Número inválido! Por favor, digite um número entre 1 e {len(alunos)}.")
    # ers
    