# Crypto.org Balance Exporter

Queries a Crypto.org Mainnet delegator address and exports its balances as metrics.

## Metrics

| Metric name | Description |
| --- | --- |
| balance | Amount of liquid CRO at delegator address |
| bonded_balance | Total amount of delegated CRO at delegator address |
| total_balance | Total amount of CRO owned by delegator address |

## Running in Python

```
export ADDRESS=cro1s********
python3 main.py
```
