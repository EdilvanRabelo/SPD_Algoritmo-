# Implemente um sistema de verificação se a data é feriado.
# Verificar na lista quais datas fazem parte do feriado nacional.  
# Receber uma data.
# Se a data for feriado, mostrar uma mensagem informando o dia e o mês feriado.
# Se a data for normal, mostrar uma mensagem informando que não é feriado.

# Dicionário de feriados nacionais.
feriados = {
    "01/01": "Ano Novo",
    "21/04": "Tiradentes",
    "01/05": "Dia do Trabalho",
    "07/09": "Independência do Brasil",
    "12/10": "Nossa Senhora da Aparecida",
    "02/11": "Finados",
    "15/11": "Proclamação da República",
    "25/12": "Natal"
}

while True:
    # solicita a data ao usuário    
    data = input("Digite uma data no formato DD/MM: ")

    # Verifica se a data está no formato correto
    if len(data) != 5 or data[2] != "/":
        print("Formato inválido. Por favor, use o formato DD/MM.")
        continue

    # Verifica se os valores são números
    dia, mes = data.split("/")
    if not dia.isdigit() or not mes.isdigit():
        print("Valores inválidos. Por favor, use números para o dia e mês.")
        continue

    # Verifica se a data é válida
    if int(dia) < 1 or int(dia) > 31 or int(mes) < 1 or int(mes) > 12:
        print("Data inválida. Por favor, use uma data válida.")
        continue

    # Verifica se a data é feriado
    if data in feriados:
        print(f"A data {data} é feriado: {feriados[data]}")
    else:
        print(f"A data {data} é normal.")

    # Pergunta ao usuário se deseja continuar
    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() != "s":
        break