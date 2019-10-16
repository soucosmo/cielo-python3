
from .objectJSON import ObjectJSON

class CreditCard(ObjectJSON):

    def __init__(self, security_code, brand):

        self.card_number = None
        self.holder = None
        self.expiration_date = None
        self.security_code = security_code
        self.save_card = None
        self.brand = brand
        self.card_token = None
        self.customer_name = None


    def update_return(self, response_return):

        self.card_token = response_return['CardToken']
