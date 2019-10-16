
from .base import Base

class UpdateSale(Base):

    def __init__(self, type, merchant, environment):

        super(UpdateSale, self).__init__(merchant)

        self.environment = environment
        self.type = type
        self.service_tax_amount = None
        self.amount = None

    def execute(self, payment_id):

        uri = '{}1/sales/{}/{}'.format(self.environment.api, payment_id, self.type)

        params = {}

        if self.amount:
            params['amount'] = self.amount

        if self.service_tax_amount:
            params['serviceTaxAmount'] = self.service_tax_amount

        return self.send_request('PUT', uri, params=params)
