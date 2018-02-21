import json
import falcon
from ethereum.tools import keys
from ..config import DECIMALS
from ..helpers import eth_helper


class RawTransaction(object):
    def on_post(self, req, resp):
        tx_data = str(req.body['tx_data'])
        error, tx_hash = eth_helper.raw_transaction(tx_data)

        if error is None:
            message = {
                'success': True,
                'tx_hash': tx_hash,
                'message': 'Transaction initiated successfully.'
            }
        else:
            message = {
                'success': False,
                'error': error,
                'message': 'Error occurred while initiating the transaction.'
            }
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(message)
