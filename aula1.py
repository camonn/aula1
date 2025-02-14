# Lista para armazenar os dados das pessoas
pessoas = []

# Função para adicionar as pessoas
def adicionar_pessoa(altura, genero):
    pessoas.append({'altura': altura, 'genero': genero})

# Exemplo de adicionar 15 pessoas
adicionar_pessoa(1.80, 'Masculino')
adicionar_pessoa(1.55, 'Feminino')
adicionar_pessoa(1.70, 'Masculino')
adicionar_pessoa(1.65, 'Feminino')
adicionar_pessoa(1.90, 'Masculino')
adicionar_pessoa(1.60, 'Feminino')
adicionar_pessoa(1.75, 'Masculino')
adicionar_pessoa(1.68, 'Feminino')
adicionar_pessoa(1.82, 'Masculino')
adicionar_pessoa(1.58, 'Feminino')
adicionar_pessoa(1.77, 'Masculino')
adicionar_pessoa(1.63, 'Feminino')
adicionar_pessoa(1.85, 'Masculino')
adicionar_pessoa(1.50, 'Feminino')
adicionar_pessoa(1.78, 'Masculino')

# Função para calcular a maior e a menor altura
def calcular_alturas():
    maior_altura = 0
    menor_altura = float('inf')

    for pessoa in pessoas:
        if pessoa['altura'] > maior_altura:
            maior_altura = pessoa['altura']
        if pessoa['altura'] < menor_altura:
            menor_altura = pessoa['altura']

    return maior_altura, menor_altura

# Função para calcular a média de altura dos homens
def media_altura_masculino():
    soma_alturas = 0
    quantidade_masculino = 0

    for pessoa in pessoas:
        if pessoa['genero'] == 'Masculino':
            soma_alturas += pessoa['altura']
            quantidade_masculino += 1

    if quantidade_masculino > 0:
        return soma_alturas / quantidade_masculino
    else:
        return 0

# Função para contar o número de mulheres
def contar_feminino():
    quantidade_feminino = 0

    for pessoa in pessoas:
        if pessoa['genero'] == 'Feminino':
            quantidade_feminino += 1

    return quantidade_feminino

# Exibição dos resultados
maior_altura, menor_altura = calcular_alturas()
media_masculino = media_altura_masculino()
numero_feminino = contar_feminino()

# Exibindo as respostas no console
print(f'Maior altura: {maior_altura} metros')
print(f'Menor altura: {menor_altura} metros')
print(f'Média de altura dos homens: {media_masculino:.2f} metros')
print(f'Número de mulheres: {numero_feminino}')
