# estrutura de dados 

# variáveis  - listas  - tuplas  -  diocionários e conjuntos
# variável cabe apenas 1 dado
nome  = 'Bea'
sobrenome  =  'Lima'
# palavra = estrutura de dados -  guardar dados


# lista  =  [] # lista vazia 
# nomes  =  ['ana','fernando','felix'] # lista do tipo texto
# numero = [1,2,3,6,6] # numeros inteiros]
# boeleana = [True, False, False] # lista boleana
# reais =  [5.0,3.6,8.1] # lista float
# lista_mista = [5.2,'texto',True,50] # lista mista 

# print(lista_mista[-4] * lista_mista[3]) 



lista_vendas  =  [4000,5000,6000,7000]
lista_vendas[0] = 50000
# métodos e funções oara manipular  
lista_vendas  =  [4000,5000,6000,7000]

# posso alterar manualmente ele e eleminar  o 

# alteram a lista 
lista_vendas[0] = 50000
lista_vendas.insert(2,200)
print(lista_vendas)

# inserir dados na minha lista 

lista_vendas.append(1000)
print(lista_vendas)

# extend pode inserir varios dados 
lista_vendas.extend([10,20,30])
print(lista_vendas)

# += inseri vários dados de uma só vez 

lista_vendas+=(20,30,30,0,50)
print(lista_vendas)


# --------------------------------------
# deletar o dado

# remove -  pop  -  del 

lista_vendas.remove(7000)
print(lista_vendas)

lista_vendas.pop()
print(lista_vendas)

lista_vendas.pop(0)
print(lista_vendas)

del lista_vendas[1]

print(lista_vendas)


# --------------------------

# função de verificação:

print(sum(lista_vendas))

print(len(lista_vendas))

print(max(lista_vendas))

print(min(lista_vendas))

l =[1,2,3,6]
c =  l.copy()
l.clear()
print(l)

# ----------

print(dir(lista_vendas))

# ORGANIZAR A LISTA
lista_vendas.sort(reverse=True )

print(lista_vendas)


# COUNT 

lista  =  [1,2,2,2,4,5,60]


# identificar onde o valor esta posicionado
print(lista.index(1))

# contar quantos tem de um determinado valor
print(lista.count(4))

# index 


