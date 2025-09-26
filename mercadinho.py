

Banco_de_dados = { "login" : "p",
"senha" : 123
                      
                      }



## solicitação de digitação


print("E-commerce Z")
print("Acesse o sistema com o login e senha")
input_login = input("login : ")
input_senha = int(input("senha : "))


## produtos 


if input_login == Banco_de_dados ["login"] and input_senha == Banco_de_dados ['senha'] :
        print("Bem - vindo ao E-commerce Z")

        produtos = ["", "SSD", "HD", "fone"]
        valores = [0, 200, 500, 250]
        produto_1 = int(input ("Id do produto : "))
        produto_2 = int(input ("Id do produto : "))
        produto_3 = int(input ("Id do produto : "))

        carrinho = []
        meu_total = []

## inserir produtos 


        carrinho.append(produtos[produto_1])
        carrinho.append(produtos[produto_2])
        carrinho.append(produtos[produto_3])
## valores vão a lista de valores
        meu_total.append(valores[produto_1])
        meu_total.append(valores[produto_2])
        meu_total.append(valores[produto_3])

        total = sum (meu_total)


        ## vizualizar o processo

        print("PRODUTOS", carrinho)
        print("TOTAL A PAGAR R$", total)
        print("****" *10)

        ## escolha de pagamento

        pagamento = ["", "PIX", "CC", "CD","PYPALL"]
        escolha_f = int(input( '''
                                
                                1- PIX 
                                2- CC
                                3- CD
                                4- PYPALL
                                
                                ''' ))
        print("sua forma de pagamento é", pagamento [escolha_f])
        print('--------------OBRIGADO E VOLTE SEMPRE!------------')
else: 
        print('digite algo valido, senha incorreta')