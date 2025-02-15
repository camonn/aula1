
alturas = []
generos = []
altura_menor = float('inf')
altura_maior = float('-inf')
total_masculino = 0
total_feminino = 0
soma_altura_masculino = 0


for i in range(1, 16):
    print(f"Pessoa {i}:")
    altura = float(input("Digite a altura (em metros): "))
    genero = input("Digite o gênero (Masculino/Feminino): ").strip().lower()

    
    alturas.append(altura)
    generos.append(genero)

    
    if altura > altura_maior:
        altura_maior = altura
    if altura < altura_menor:
        altura_menor = altura

    
    if genero == "masculino":
        soma_altura_masculino += altura
        total_masculino += 1
    elif genero == "feminino":
        total_feminino += 1


media_altura_masculino = soma_altura_masculino / total_masculino if total_masculino > 0 else 0


print("\nResultados:")
print(f"A maior altura do grupo é: {altura_maior} metros")
print(f"A menor altura do grupo é: {altura_menor} metros")
print(f"A média de altura do gênero Masculino é: {media_altura_masculino:.2f} metros")
print(f"O número de pessoas do gênero Feminino é: {total_feminino}")
