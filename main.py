# sistema de mercado


print('MERCADO Z')
produtos = ['','1 arroz',' 2 feijão',' 3 macarrão',' 4 leite',' 5 chocolate']
valores = [0,10.0, 15.0, 5.0, 8.50,11.25]
carrinho = []
meu_total = []


pedir = input('Deseja pedir?')
pedido = pedir == 'sim'
print('Resposta:',pedido)


# escolhendo o produto
print(produtos)


produto_1 = int(input('Digite o Id 1 2 3 4 do produto: '))
produto_2 = int(input('Digite o Id 1 2 3 4 do produto: '))
produto_3 = int(input('Digite o Id 1 2 3 4 do produto: '))
produto_4 = int(input('Digite o Id 1 2 3 4 do produto: '))


# add ao carrinho
carrinho.append(produtos[produto_1])
carrinho.append(produtos[produto_2])
carrinho.append(produtos[produto_3])
carrinho.append(produtos[produto_4])


# valores dos produtos estão entrando na lista
meu_total.append(valores[produto_1])
meu_total.append(valores[produto_2])
meu_total.append(valores[produto_3])
meu_total.append(valores[produto_4])


soma = sum(meu_total)


print('Seu carrinho', carrinho)
print('Total R$', soma)


print('Escolha a forma de pagamento')


pagamentos  = ['id  0   PIX',' id 1  CC','id  2  CD']

print(pagamentos)
escolha = int(input('Escolha a forma: '))
print('Sua froma de pagamento é:', pagamentos [escolha])
print('Obrigada Volte sempre!')





