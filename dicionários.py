### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
vendas: list = [] 
produto1 = {'nome': 'arroz',
    'quantidade': 12,
    'preço': 20.6
    }
produto2 = {'nome': 'alface',
    'quantidade': 10,
    'preço': -2.5
    }
vendas.append(produto1)
vendas.append(produto2)
for produto in vendas:
    if produto['quantidade'] >= 0 and produto['preço'] >= 0:
        print(f'DaDOS INVÁLIDOS em {produto['nome']}')
    else:
        print('DaDOS VÁLIDOS')



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
usuarios_teste = [
    {"nome": "Lucas Silva", "idade": 25, "email": "lucas.silva@email.com"},        # Válido
    {"nome": "Mariana Costa", "idade": 17, "email": "mari.costa@gmail.com"},       # Erro: Menor de idade
    {"nome": "Roberto Souza", "idade": 66, "email": "roberto.souza@outlook.com"},   # Erro: Maior de 65
    {"nome": "Ana Souza", "idade": 40, "email": "ana.souza@invalid"},              # Erro: Email mal formatado
    {"nome": "Carlos Oliveira", "idade": 18, "email": "carlos@empresa.com.br"},    # Válido (limite inferior)
    {"nome": "Beatriz Lima", "idade": 65, "email": "b_lima@provedor.net"},         # Válido (limite superior)
    {"nome": "Fernando Dias", "idade": 30, "email": "fernando.dias.com"},          # Erro: Email sem @
    {"nome": "Julia Martins", "idade": 22, "email": "@instagram.com"}
]
usuarios_validos = []
from validate_email import validate_email
for usuario in usuarios_teste:
    if usuario['idade'] < 18 or usuario['idade'] > 65:
        print(f'{usuario['nome']} não possui idade requerida.')
    
    else:
        is_valid = validate_email(usuario['email'])
        if not is_valid:
            print(f"{usuario['nome']} com email inválido.")
        else:
            usuarios_validos.append(usuario)
            
        
        
print(usuarios_teste)

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacoes = [
    {"id": 1, "valor": 8500, "hora": 14},     # Normal
    {"id": 2, "valor": 12000, "hora": 11},    # Suspeita: valor alto
    {"id": 3, "valor": 4500, "hora": 22},     # Suspeita: fora do horário
    {"id": 4, "valor": 25000, "hora": 2},     # Suspeita: valor + horário
    {"id": 5, "valor": 9999, "hora": 10},     # Normal
    {"id": 6, "valor": 10001, "hora": 16},    # Suspeita: valor alto
    {"id": 7, "valor": 300, "hora": 7},       # Suspeita: antes das 9h
    {"id": 8, "valor": 7600, "hora": 18},     # Normal (18h ainda permitido)
    {"id": 9, "valor": 15000, "hora": 19},    # Suspeita
    {"id": 10, "valor": 5000, "hora": 13}     # Normal
]
for transacao in transacoes:
    if transacao['valor'] > 10000 or transacao['hora'] > 18 or transacao['hora'] < 9:
        print(f"Transação {transacao['id']} é suspeita.")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "A tecnologia faz parte do cotidiano das pessoas e está presente em diversas áreas da sociedade. Muitas pessoas utilizam a tecnologia para estudar, trabalhar, se comunicar e se divertir. O avanço da tecnologia também trouxe mudanças importantes para a educação e para o mercado de trabalho. Por outro lado, algumas pessoas acreditam que o uso excessivo da tecnologia pode causar problemas sociais e dificuldades de comunicação."
texto = texto.lower()
texto = texto.replace('.', '')
texto = texto.replace(',', '')
palavras = texto.split()
dicionario = {}

for palavra in palavras:
    if palavra not in dicionario:
        dicionario[palavra] = 1
    else:
        dicionario[palavra] += 1
print(dicionario)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [42, 7, 89, 15, 63, 28, 91, 3, 56, 74, 20]
numeros.sort()
n_em_escala = []
for n in numeros:
    e = (n - min(numeros)) / (max(numeros) - min(numeros))
    n_em_escala.append(f'{e:.2f}')
print(n_em_escala)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
usuarios = [
    {"nome": "Lucas", "idade": 17, "email": "lucas@email.com"},
    {"nome": "Mariana", "idade": 16},
    {"nome": "Carlos", "email": "carlos@gmail.com"},
    {"nome": "Ana", "idade": 18, "email": "ana@yahoo.com"},
    {"nome": "Fernanda"},
    {"nome": "Roberto", "idade": 20},
    {"nome": "Julia", "email": "julia@outlook.com"},
    {"nome": "Beatriz", "idade": 19, "email": "beatriz@email.com"}
]
for usuario in usuarios:
    if 'nome' not in usuario or 'idade' not in usuario or 'email' not in usuario:
        print(f"{usuario['nome']} tem algum campo vazio.")


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3500},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 120},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 200},
    {"produto": "Camiseta", "categoria": "Roupas", "valor": 80},
    {"produto": "Calça Jeans", "categoria": "Roupas", "valor": 150},
    {"produto": "Tênis", "categoria": "Roupas", "valor": 300},
    {"produto": "Arroz", "categoria": "Alimentos", "valor": 35},
    {"produto": "Feijão", "categoria": "Alimentos", "valor": 28},
    {"produto": "Refrigerante", "categoria": "Alimentos", "valor": 12},
    {"produto": "Livro Python", "categoria": "Livros", "valor": 95},
    {"produto": "Livro Matemática", "categoria": "Livros", "valor": 110}
]
vendasCategoria = {}
for produto in vendas:
    if produto['categoria'] not in vendasCategoria:
        vendasCategoria[produto['categoria']] = produto['valor']
    else:
        vendasCategoria[produto['categoria']] += produto['valor']
print(vendasCategoria)
