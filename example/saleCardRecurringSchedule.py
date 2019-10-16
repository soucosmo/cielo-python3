#-*- coding: utf-8 -*-s

import sys
sys.path.insert(0, "./")

from cieloApi3 import *

import json

# Configure o ambiente
environment = Environment(sandbox=True)

# Configure seu merchant, para gerar acesse: https://cadastrosandbox.cieloecommerce.cielo.com.br/
merchant = Merchant('MerchantId', 'MerchantKey')

# Crie uma instância de Sale informando o ID do pagamento
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador rec programada')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment(False)
recurrent_payment.interval = INTERVAL_SEMIANNUAL
recurrent_payment.start_date = '2015-06-01'
recurrent_payment.end_date = '2019-12-01'

# Crie uma instância de Payment informando o valor do pagamento
sale.payment = Payment(1500)
sale.payment.recurrent_payment = recurrent_payment
sale.payment.credit_card = credit_card

# Cria instância do controlador do ecommerce
cielo_ecommerce = CieloEcommerce(merchant, environment)

# Criar a venda e imprime o retorno
response_create_sale = cielo_ecommerce.create_sale(sale)
print('----------------------response_create_sale----------------------')
print(json.dumps(response_create_sale, indent=2))
print('----------------------response_create_sale----------------------')
