# Criar um metodo gerar senha para usar o banheiro coletivo.
# Solicitar o usuario identificaçao do sexo (M ou F).
# Gerar uma senha de 4 digitos de acordo com o sexo.
# Mostrar a senha gerada.
# Se o sexo for masculino, a senha deve ser iniciada com M. 
# Se o sexo for feminino, a senha deve ser iniciada com F.
# Se o sexo for diferente de masculino ou feminino, mostrar uma mensagem de erro.

# Importa a biblioteca para trabalhar com datas.
from datetime import datetime

# Solicita ao usuário o sexo do usuario
sexo = input("Digite seu sexo (M ou F): ")

# Verifica se o sexo é masculino ou feminino
if sexo.upper() == "M":
    # Gera uma senha de 4 dígitos iniciada com M
    senha = "M" + str(datetime.now().microsecond)[-4:]
elif sexo.upper() == "F":
    # Gera uma senha de 4 dígitos iniciada com F
    senha = "F" + str(datetime.now().microsecond)[-4:]
else:
    # Se o sexo for diferente de masculino ou feminino, mostra uma mensagem de erro
    print("Sexo inválido!")
    senha = None

# Mostra a senha gerada
if senha:
    print(f"Senha gerada: {senha}") 