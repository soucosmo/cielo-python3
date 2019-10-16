
INTERVAL_MONTHLY = "Monthly"
INTERVAL_BIMONTHLY = "Bimonthly"
INTERVAL_QUARTERLY = "Quarterly"
INTERVAL_SEMIANNUAL = "SemiAnnual"
INTERVAL_ANNUAL = "Annual"

class RecurrentPayment(object):

    def __init__(self, authorize_now=True):

        self.authorize_now = authorize_now
        self.start_date = None
        self.end_date = None
        self.interval = None
        self.recurrent_payment_id = None
