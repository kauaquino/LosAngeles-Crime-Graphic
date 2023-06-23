import csv
import matplotlib.pyplot as plt

# Abre o arquivo CSV contendo os dados dos crimes
crimes = open('dataset.csv')

# Cria um leitor de CSV para ler o arquivo
lendoCrimes = csv.reader(crimes, delimiter=",")

# Cria uma lista vazia para armazenar as localizações dos crimes
listaLocal = []

# Percorre cada linha do arquivo CSV
for linha in lendoCrimes:
    # Adiciona a localização do crime à lista
    listaLocal.append(linha[5])

# Cria um dicionário para armazenar as frequências das localizações
frequencia = {}

# Percorre cada localização na lista, se tiver a localização contabiliza 1 valor, se não ele inicia no valor 1
for string in listaLocal:
    if string in frequencia:
        frequencia[string] += 1
    else:
        frequencia[string] = 1

# Cria uma lista formatada com as localizações e as quantidades de crimes
strings_quantidade = [f"{string}: {quantidade}" for string, quantidade in frequencia.items()]

# Separa as localizações e quantidades de forma separada para chamar "LOCALIZACAO" : "VALOR"
labels = [item.split(':')[0] for item in strings_quantidade]
values = [int(item.split(':')[1]) for item in strings_quantidade]

# Gera um gráfico com as localizações e quantidades
plt.bar(labels, values)
plt.xticks(rotation=90)
plt.xlabel('Região')
plt.ylabel('Quantidade')
plt.title('Quantidade de crimes por Região de Los Angeles')
plt.tight_layout()
plt.show()