# Chainabuse Address Screening

A Python-based blockchain security pipeline that checks Ethereum address against Chainabuse's community-reported abuse database.

## Objective

The project demonstrates how an Ethereum address can be screened for community-reported scam or abuse reports using the Chainabuse API.

Chainabuse reports are treated as intelligence signals and not as absolute proof that an address is malicious or safe.

## Data Source

**Provider:** Chainabuse

**Endpoint:**

```text
GET https://api.chainabuse.com/v0/reports
```

**Chain:** ETH

## Pipeline

Ethereum Address<br>
       |<br>
       v<br>
Chainabuse API<br>
       |<br>
       v<br>
Community Reports<br>
       |<br>
       v<br>
Report Count + Report Details<br>
       |<br>
       v<br>
Structured Output<br>

## Project Structure

chainabuse-address-screening/<br>
│<br>
├── data/<br>
│   ├── addresses.csv<br>
│   └── chainabuse_output.csv<br>
│<br>
├── .env<br>
├── .gitignore<br>
├── chainabuse.py<br>
└── README.md<br>

## Input

Ethereum addresses are stored in:
```
data/addresses.csv
```

**Example:**
```
address
0x...
0x...
```

## Authentication

The Chainabuse API key is stored in an environment variable:
```
CHAINABUSE_API_KEY=your_api_key_here
```

## API Test

The API was successfully tested against an Ethereum address.
```
HTTP Status: 200

Response:
{
    "count": 0,
    "reports": []
}
```


### final note

For this task, I recommend **not creating `chainabuse_output.csv` yet**, because we only performed the single-address test and it returned zero reports. The README accurately documents what we actually verified.

That completes the Chainabuse task.