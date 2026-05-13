#try: #se der certo
#except: #se der errado
#else: #se der certo
#finally: #independente
#numero = 10
#if isinstance(numero, int):
  #  print('é inteiro')
#else: 
 #   pass
# Solicita ao usuário que digite seu nome
while True:
    nome_usuario: str = input('Digite seu nome: ')
    # Verifica se o nome está vazio
    if len(nome_usuario) == 0:
        print("O nome não pode estar vazio.")
        continue
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome_usuario):
        print("O nome não deve conter números.")
        continue
    else:
        print("Nome válido:", nome_usuario)
        break


# Solicita ao usuário que digite o valor do seu salário e converte para float

while True:
    salario: float = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
        continue
    else:
        break

while True:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus >= 0:
        break
    else:
        print("Entrada inválida para o bônus. Por favor, digite um número positivo.")
        continue

bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome_usuario}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

# 4) Calcule o valor do bônus final
bonus_final: float = bonus * salario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Nome: {nome_usuario}\nSalário: {salario}\nBônus:{bonus_final}')