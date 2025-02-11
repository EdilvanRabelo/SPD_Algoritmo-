# Implemente um sistema de verificação se a data é feriado.
# verificar na lista quais datas fazem parte do feriado nacional.  
# receber uma data 
# se a data for feriado, mostrar uma mensagem informando o dia e o mes feriado.
# se a data for normal, mostrar uma mensagem informando que não é feriado.

# Dicionário de feriados nacionais
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

# solicita a data ao usuario    
data = input("Digite uma data no formato DD/MM: ")

# Verifica se a data é feriado
if data in feriados:
    print(f"A data {data} é feriado: {feriados[data]}")
else:
    print(f"A data {data} é normal.")       
                                                                 