#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import requests
from flask import Flask, Response
from prometheus_client import generate_latest, Gauge, Summary

app = Flask(__name__)

# which port to run the exporter on
PORT = 26661

# flask debugging
DEBUG = os.environ.get("DEBUG")

# sanity checks
address = os.environ.get("ADDRESS")
if not address:
    raise Exception("ADDRESS is not set!")
elif not address.startswith("cro1s"):
    raise Exception("ADDRESS should start with 'cros1s'")

# where to send the request
api_url = f"https://crypto.org/explorer/api/v1/accounts/{address}"

# exported metrics
timer = Summary('request_processing_seconds', 'Time spent processing request')
balance = Gauge('balance', 'Amount of liquid CRO at delegator address')
bonded = Gauge('bonded_balance', 'Total amount of delegated CRO at delegator address')
totals = Gauge('total_balance', 'Total amount of CRO owned by delegator address')


@app.route('/metrics', methods=['GET'])
def get_data():
    """Send HTTP request to Crypto.org and retrieve balance"""

    # query Crypto.org
    with timer.time():
        resp = requests.get(api_url)
        resp.raise_for_status()
        data = resp.json()["result"]

        f = lambda result: float(data[result][0]["amount"])/100.0
        balance.set(f("balance"))
        bonded.set(f("bondedBalance"))
        totals.set(f("totalBalance"))

    return Response(generate_latest())


if __name__ == '__main__':
    logging.basicConfig()
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)

