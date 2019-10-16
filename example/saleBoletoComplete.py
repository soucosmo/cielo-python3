#-*- coding: utf-8 -*-s

import sys
sys.path.insert(0, "./")

from cielo import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('555')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador Teste')

# Crie uma instância de Payment informando o valor do pagamento
payment = Payment(15700)
payment.type = PAYMENTTYPE_BOLETO

payment.provider = PROVIDER_BANCO_DO_BRASIL
payment.address = 'Rua Alegria N: 3 Bairro: Rosa São Paulo-SP'
payment.boleto_number = '123'
payment.assignor = 'Empresa Teste'
payment.demonstrative = 'Demonstrativo Teste'
payment.expiration_date = '2017-06-11'
payment.identification = '11884926754'
payment.instructions = 'Aceitar somente até a data de vencimento, após essa data juros de 1% dia.'

sale.payment = payment

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print('----------------------response_create_sale----------------------')
print json.dumps(response_create_sale, indent=2)
print('----------------------response_create_sale----------------------')

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer uma consulta do pagamento
response_get_sale = cielo_ecommerce.get_sale(payment_id)
print('----------------------response_get_sale----------------------')
print json.dumps(response_get_sale, indent=2)
print('----------------------response_get_sale----------------------')

print('\r\nLink Boleto:', sale.payment.url, '\r\n')
