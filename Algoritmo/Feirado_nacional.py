# Implemente um sistema de verificação se a data é feriado.
# verificar na lista quais datas fazem parte do feriado nacional.  
# receber uma data 
# se a data for feriado, mostrar uma mensagem informando o dia e o mes feriado.
# se a data for normal, mostrar uma mensagem informando que não é feriado.

# lista de feriados nacionais
feriados = ["01/01", "21/04", "01/05", "07/09", "12/10", "02/11", "15/11", "25/12"] 

# solicita a data ao usuario    
data = input("Digite uma data no formato DD/MM: ")

# verifica se a data eh feriado 
if data in feriados:    
    print(f"A data {data} é feriado.")
else:                                    
    print(f"A data {data} é normal.")                                                                           