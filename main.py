# variavel palavra  =  valor
# lista = [] ou l =  list(range(1,11))
# tupla = ()  ou t =  tuple(range(1,11))
# conjun = {}  ou  c = set(range(1,11))
# dicionario = {'a':10,'b':20}  ou  d = dict(a =10 , b = 20)

#DESAFIO

##crie um e-commerce com a estrutura de dicionários.

## livros, tablets e fones de ouvidos

#livros = 
#tablets =
#fones_de_ouvido = 

#my_dicionary = ("livros", "tablets", "fones_de_ouvido")



ecommerce = {
    
    'livros' : {
        
        'A':50.0,
        'B':50.0,
        'C':35.0,
     
        },
    'eletronicos':{
        
        'Tablets':300.00,
        'Fone':60.00,
             
        }
   
    
}

secao1 = input('Digite o seção 1 =')
secao2 = input('Digite o seção 2 =')

produto1 = input('Digite o produto 1')
produto2 = input('Digite o produto 2')

carrinho = [produto1, produto2]
valores =  [ecommerce[secao1][produto1],ecommerce[secao2][produto2]]
soma =  sum(valores)

print(carrinho)
print('R$', soma)