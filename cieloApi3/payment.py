
from .objectJSON import ObjectJSON

PAYMENTTYPE_CREDITCARD = "CreditCard"
PAYMENTTYPE_DEBITCARD = "DebitCard"
PAYMENTTYPE_ELECTRONIC_TRANSFER = "ElectronicTransfer"
PAYMENTTYPE_BOLETO = "Boleto"

PROVIDER_BRADESCO = "Bradesco"
PROVIDER_BANCO_DO_BRASIL = "BancoDoBrasil"
PROVIDER_SIMULADO = "Simulado"

class Payment(ObjectJSON):

    def __init__(self, amount, installments = 1):

        self.amount = amount
        self.service_tax_amount = None
        self.installments = installments
        self.interest = None
        self.capture = None
        self.authenticate = None
        self.recurrent = None
        self.recurrent_payment = None
        self.credit_card = None
        self.proof_of_sale = None
        self.authorization_code = None
        self.soft_descriptor = None
        self.return_url = None
        self.provider = None
        self.payment_id = None
        self.tid = None
        self.type = None
        self.received_date = None
        self.captured_amount = None
        self.captured_date = None
        self.currency = None
        self.country = None
        self.return_code = None
        self.return_message = None
        self.status = None
        self.links = None
        self.extra_data_collection = None
        self.expiration_date = None
        self.url = None
        self.number = None
        self.bar_code_number = None
        self.digitable_line = None
        self.address = None

        #Boleto
        self.boleto_number = None
        self.assignor = None
        self.demonstrative = None
        self.identification = None
        self.instructions = None


    def prepare(self):

        if self.credit_card:
            self.type = PAYMENTTYPE_CREDITCARD
