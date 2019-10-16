class Environment(object):

    def __init__(self, sandbox):

        # Production
        if not sandbox:
            self.api = 'https://api.cieloecommerce.cielo.com.br/'
            self.api_query = 'https://apiquery.cieloecommerce.cielo.com.br/'
        else:
            self.api = 'https://apisandbox.cieloecommerce.cielo.com.br/'
            self.api_query = 'https://apiquerysandbox.cieloecommerce.cielo.com.br/'
