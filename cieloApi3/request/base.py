import uuid, json

from future.utils import raise_with_traceback
from requests import Request, Session

class Base(object):

    def __init__(self, merchant):

        self.merchant = merchant

    def send_request(self, method, uri, data=None, params=None):

        s = Session()

        body = data

        headers = {
            'User-Agent': "CieloEcommerce/3.0 Python SDK",
            'RequestId': str(uuid.uuid4()),
            'MerchantId': self.merchant.id,
            'MerchantKey': self.merchant.key
        }

        if not body:
            headers['Content-Length'] = '0'
        else:
            headers["Content-Type"] = "application/json"

            if not isinstance(data, dict):
                body = body.toJSON()

        req = Request(method, uri, data=body, headers=headers, params=params)

        prep = s.prepare_request(req)

        response = s.send(prep)

        if 'json' in response.headers['Content-Type'].lower():
            answers = response.json()
        else:
            answers = [{
                'Code': str(response.status_code),
                'Message': response.text
            }]

        if response.status_code >= 400:
            errors = []

            for answer in answers:
                errors.append('\r\n * [%s] %s\r\n' % (answer['Code'], answer['Message']))

            data_send = json.loads(body or 'null')

            raise_with_traceback(Exception('\r\n{}\r\nMethod: {}\r\nUri: {}\r\nData: {}'.format(''.join(errors), method, response.url, json.dumps(data_send, indent=2))))

        return answers
