
from .base import Base

class CreateCardToken(Base):

    def __init__(self, merchant, environment):

        super(CreateCardToken, self).__init__(merchant)

        self.environment = environment

    def execute(self, creditCard):

        uri = '{}1/card'.format(self.environment.api)

        response = self.send_request("POST", uri, creditCard)

        creditCard.update_return(response)

        return response
