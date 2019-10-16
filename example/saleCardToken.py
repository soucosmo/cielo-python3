#-*- coding: utf-8 -*-s

import sys
sys.path.insert(0, "./")

from cielo import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '4532117080573700'
credit_card.holder = 'Comprador T Cielo'
credit_card.customer_name = 'Comprador Teste Cielo'

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_card_token = cielo_ecommerce.create_card_token(credit_card)
print('----------------------response_create_card_token----------------------')
print(json.dumps(response_create_card_token, indent=2))
print('----------------------response_create_card_token----------------------')

# Com o cartão gerado token na Cielo, já temos o Token do cartão para uma futura cobrança
new_card_token = credit_card.card_token
print('New Card Token:', new_card_token)

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('456')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Credit Card utilizando os dados de teste via token
credit_card_token = CreditCard('123', 'Visa')
credit_card_token.card_token = new_card_token

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(100)
sale.payment.credit_card = credit_card_token

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print('----------------------response_create_sale----------------------')
print(json.dumps(response_create_sale, indent=2))
print('----------------------response_create_sale----------------------')
