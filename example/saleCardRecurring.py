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
sale = Sale('789')

# Crie uma instância de Customer informando o nome do cliente
sale.customer = Customer('Comprador accept')

# Crie uma instância de Credit Card utilizando os dados de teste
# esses dados estão disponíveis no manual de integração
credit_card = CreditCard('262', 'Visa')
credit_card.expiration_date = '03/2019'
credit_card.card_number = '1234123412341231'
credit_card.holder = 'Teste Holder'

recurrent_payment = RecurrentPayment()
recurrent_payment.interval = INTERVAL_SEMIANNUAL
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





# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print('----------------------response_capture_sale----------------------')
print(json.dumps(response_capture_sale, indent=2))
print('----------------------response_capture_sale----------------------')

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print('---------------------response_cancel_sale---------------------')
print(json.dumps(response_cancel_sale, indent=2))
print('---------------------response_cancel_sale---------------------')





# Com a venda recorrente criada na Cielo, já temos o ID do pagamento recorrente
recurrent_payment_id = sale.payment.recurrent_payment.recurrent_payment_id

# Consulta informações da venda recorrente
response_get_recurrent_payment = cielo_ecommerce.get_recurrent_payment(recurrent_payment_id))
print('---------------------response_get_recurrent_payment---------------------')
print(json.dumps(response_get_recurrent_payment, indent=2))
print('---------------------response_get_recurrent_payment---------------------')

# # Desativa uma venda recorrente (Algum erro na API da Cielo, parou de funcionar)
# response_deactivate_recurrent_payment = cielo_ecommerce.deactivate_recurrent_payment(recurrent_payment_id)
# print '---------------------response_deactivate_recurrent_payment---------------------'
# print json.dumps(response_deactivate_recurrent_payment, indent=2)
# print '---------------------response_deactivate_recurrent_payment---------------------'

# # Reativa uma venda recorrente (Algum erro na API da Cielo, parou de funcionar)
# response_reactivate_recurrent_payment = cielo_ecommerce.reactivate_recurrent_payment(recurrent_payment_id)
# print '---------------------response_reactivate_recurrent_payment---------------------'
# print json.dumps(response_reactivate_recurrent_payment, indent=2)
# print '---------------------response_reactivate_recurrent_payment---------------------'
