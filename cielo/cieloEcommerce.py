
from .request.createSale import CreateSale
from .request.querySale import QuerySale
from .request.updateSale import UpdateSale
from .request.createCardToken import CreateCardToken
from .request.queryRecorrency import QueryRecorrency
from .request.deactivateRecorrency import DeactivateRecorrency
from .request.reactivateRecorrency import ReactivateRecorrency

class CieloEcommerce(object):

    def __init__(self, merchant, environment):

        self.environment = environment
        self.merchant = merchant

    def create_sale(self, sale):

        request = CreateSale(self.merchant, self.environment)

        return request.execute(sale)

    def capture_sale(self, payment_id, amount = None, service_tax_amount = None):
        request = UpdateSale('capture', self.merchant, self.environment)

        request.amount = amount
        request.service_tax_amount = service_tax_amount

        return request.execute(payment_id)

    def cancel_sale(self, payment_id, amount = None):
        request = UpdateSale('void', self.merchant, self.environment)

        request.amount = amount

        return request.execute(payment_id)

    def get_sale(self, payment_id):
        request = QuerySale(self.merchant, self.environment)

        return request.execute(payment_id)

    def create_card_token(self, creditCard):

        request = CreateCardToken(self.merchant, self.environment)

        return request.execute(creditCard)

    def get_recurrent_payment(self, recurrent_payment_id):

        request = QueryRecorrency(self.merchant, self.environment)

        return request.execute(recurrent_payment_id)

    def deactivate_recurrent_payment(self, recurrent_payment_id):

        request = DeactivateRecorrency(self.merchant, self.environment)

        return request.execute(recurrent_payment_id)

    def reactivate_recurrent_payment(self, recurrent_payment_id):

        request = ReactivateRecorrency(self.merchant, self.environment)

        return request.execute(recurrent_payment_id)


