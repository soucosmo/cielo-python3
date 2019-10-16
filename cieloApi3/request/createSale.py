
from .base import Base

class CreateSale(Base):

    def __init__(self, merchant, environment):

        super(CreateSale, self).__init__(merchant)

        self.environment = environment

    def execute(self, sale):

        uri = '{}1/sales'.format(self.environment.api)

        response = self.send_request("POST", uri, sale)

        sale.update_return(response)

        return response
