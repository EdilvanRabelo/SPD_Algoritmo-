# Criar um método para verificar se ja tenho idade para tirar CNH.
# Informar a data de nascimento.
# Verificar se a pessoa é maior de 18 anos.
# Se for, mostrar uma mensagem dizendo que ela pode tirar a CNH.    
# Se não for, mostrar uma mensagem dizendo que ainda falta x anos para tirar a CNH.

# Importa a biblioteca para trabalhar com datas.
from datetime import datetime 
def pode_tirar_cnh(data_nascimento):
    """
    Função que verifica se a pessoa pode tirar a CNH com base na data de nascimento.
    :param data_nascimento: str - Data no formato 'DD/MM/AAAA'
    :return: str - Mensagem informando se pode ou não tirar a CNH.
    """
    # Tentativa de conversão da data informada.
    try:
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        return "Formato inválido! Use DD/MM/AAAA."

    # Obtém a data atual.
    hoje = datetime.today()
    
    # Calcula a idade da pessoa.
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    # Verifica se já pode tirar a CNH.
    if idade >= 18:
        return f"Você tem {idade} anos e já pode tirar sua primeira CNH!"
    else:
        return f"Você tem {idade} anos. Ainda faltam {18 - idade} anos para tirar a CNH."

# Entrada do usuário.
data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ")
print(pode_tirar_cnh(data_nasc))