import csv

pessoas = []
with open('dados.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        nome, idade = row
        pessoas.append({"nome": nome, "idade": int(idade)})

nome_usuario = input("Digite o nome: ")

encontrado = False
idade_usuario = None
mais_velho = True

for pessoa in pessoas:
    if pessoa['nome'].lower() == nome_usuario.lower():
        encontrado = True
        idade_usuario = pessoa['idade']
        mais_velho = all(p['idade'] <= idade_usuario for p in pessoas)
        break

if encontrado:
    print(f"{nome_usuario} tem {idade_usuario} anos.")
    if mais_velho:
        print(f"{nome_usuario} é a pessoa mais velha da lista!")
    else:
        print(f"{nome_usuario} não é a pessoa mais velha da lista.")
else:
    print(f"{nome_usuario} não está na lista.")
