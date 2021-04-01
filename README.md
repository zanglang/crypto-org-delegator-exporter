# Crypto.org Balance Exporter

Queries a Crypto.org Mainnet delegator address and exports its balances as metrics.

## Metrics

| Metric name | Description |
| --- | --- |
| balance | Amount of liquid CRO at delegator address |
| bonded_balance | Total amount of delegated CRO at delegator address |
| total_balance | Total amount of CRO owned by delegator address |
| request_processing_seconds | Time taken for HTTP request to be served by https://crypto.org |

## Running in Docker

```
docker pull zanglang/crypto-org-delegator-exporter:latest
docker run -d -p 26661:26661 \
    -e ADDRESS=cros1***** \
    --name crypto-org-exporter \
    zanglang/crypto-org-delegator-exporter
```

## Running in Python

```
export ADDRESS=cro1s********
export DEBUG=1  # enables debug logs
python3 main.py
```

## Example Prometheus Config

```
scrape_configs:
- job_name: my-wallet
  static_configs:
  - targets: ['localhost:26661']
    labels:
      instance: delegator
```
