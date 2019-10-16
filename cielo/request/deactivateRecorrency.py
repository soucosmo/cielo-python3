
from .base import Base

class DeactivateRecorrency(Base):

    def __init__(self, merchant, environment):

        super(DeactivateRecorrency, self).__init__(merchant)

        self.environment = environment

    def execute(self, payment_id):

        uri = '{}1/RecurrentPayment/{}/Deactivate'.format(self.environment.api_query, payment_id)

        return self.send_request("PUT", uri)
