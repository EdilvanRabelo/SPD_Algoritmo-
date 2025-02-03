# Verificação de idade para tirar CNH

from datetime import datetime # Importa a biblioteca para trabalhar com datas

def pode_tirar_cnh(data_nascimento):
    """
    Função que verifica se a pessoa pode tirar a CNH com base na data de nascimento.
    :param data_nascimento: str - Data no formato 'DD/MM/AAAA'
    :return: str - Mensagem informando se pode ou não tirar a CNH.
    """
    # Tentativa de conversão da data informada
    try:
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        return "Formato inválido! Use DD/MM/AAAA."

    # Obtém a data atual
    hoje = datetime.today()
    
    # Calcula a idade da pessoa
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    # Verifica se já pode tirar a CNH
    if idade >= 18:
        return f"Você tem {idade} anos e já pode tirar sua primeira CNH!"
    else:
        return f"Você tem {idade} anos. Ainda faltam {18 - idade} anos para tirar a CNH."

# Entrada do usuário
data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ")
print(pode_tirar_cnh(data_nasc))