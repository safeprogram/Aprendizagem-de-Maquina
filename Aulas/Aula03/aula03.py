setMeuConjunto =set()
setMeuConjunto.add('a')
setMeuConjunto.add('d')
setMeuConjunto.add('b')
setMeuConjunto.add(2)
print(setMeuConjunto)

setMeuConjunto = set()
setMeuConjunto.add('a')
setMeuConjunto.add('d')
setMeuConjunto.add('a')
print (setMeuConjunto)

lisMinhaLista = [1,1,1,1,2,2,21,3,4,51,23,1,2,3,5,8]
print (lisMinhaLista)
print (set(lisMinhaLista))

lista_elementos = ["Carro", "Abajur", "Moto", "Barco", "Ferro de passar roupa", "2", "Barco", "moto"]

# Converter para minúsculas para comparação sem diferenciação de maiúsculas e minúsculas
lista_minuscula = [x.lower() for x in lista_elementos]

# Ordenar a lista em ordem alfabética (considerando minúsculas)
lista_ordenada = sorted(lista_minuscula)

# Criar um conjunto para remover elementos duplicados e manter a ordem original
elementos_unicos = []
for elemento in lista_ordenada:
    if elemento not in elementos_unicos:
        elementos_unicos.append(elemento)

# Gravar a lista com elementos únicos em um arquivo
with open("elementos_unicos.txt", "w") as arquivo:
  for elemento in elementos_unicos:
    arquivo.write(elemento + "\n")


for i in range (0,10,2):
    print (i)

lstMinhaLista = [1,2,3,4,5]
for qlqNome in lstMinhaLista:
    print (qlqNome)


lstMinhaLista = [1,2,3,4,5,6,7,8,9,10]
for numero in lstMinhaLista:

    if (numero % 2 == 0):
        print (f'O numero {numero} e par.')

    else:
        print (f'O numero {numero} e impar.')

    lstMinhaLista = [(1,2),(3,4),(4,5),(5,6),(7,8)]
    print (len(lstMinhaLista))

    for item in lstMinhaLista:
        print (item)

lstMinhaLista = [(1,2),(3,4),(4,5),(5,6),(7,8)]
print (len(lstMinhaLista))

for a,b in lstMinhaLista:
    print (f'Este é o primeiro item da tupla: {a} e o segundo é: {b}')



lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip(lista1, lista2)

for x,y in resultado:

  print(f'Primeiro elemento: {x} e segundo: {y}')


lstMinhaLista1 = [1,2,3]
lstMinhaLista2 = ['a','b','c']
lstMinhaLista3 = [100,200,300]
lstMinhaLista4 = list(zip(lstMinhaLista1,lstMinhaLista2,lstMinhaLista3))
print (lstMinhaLista4)

lstMinhaLista1 = [1,2,3]
print (1 in lstMinhaLista1)

lstMinhaLista1 = [1,2,3,4,5]
print (max(lstMinhaLista1))
print (min(lstMinhaLista1))