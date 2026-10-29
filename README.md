# Simple Blockchain Transaction Demo

A small Python demonstration of how a blockchain links blocks using SHA-256 hashes. The project defines a `Block` class that stores a list of transaction strings, the previous block's hash, and the hash calculated for the current block.

> **Educational example only:** This script illustrates hash chaining; it is not a production blockchain or cryptocurrency implementation. It does not implement consensus, transaction signatures, networking, persistent storage, or tamper-resistant transaction validation.

## Requirements

- Python 3
- Python standard library only (`hashlib`)

## Run

Clone the repository and enter its directory:

```bash
git clone https://github.com/ashAKT/Blockchain.git
cd Blockchain
python3 SimpleTransaction.py
```

On Windows, you can run:

```powershell
py SimpleTransaction.py
```

The program creates a genesis block and two subsequent blocks, then prints each block's SHA-256 hash.

## How it works

The `Block` class accepts:

- `previous_hash`: the hash of the preceding block (or a genesis value for the first block).
- `transaction`: a list of transaction descriptions.
- `block_hash`: SHA-256 of the concatenated transaction strings and previous hash.

Each later block uses the preceding block's hash, demonstrating a basic hash-linked chain.

## Project files

```text
Blockchain/
└── SimpleTransaction.py
```

## Limitations

- Transactions are plain text and are not digitally signed or authenticated.
- The example does not validate blocks or enforce consensus.
- Data is held in program memory and is not persisted.
- The genesis block's previous-hash value is a demonstration string, not a cryptographic genesis-block protocol.
- This is not suitable for real financial transactions or security-critical applications.

## Learning references

- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
- [SHA-256 overview (NIST)](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)

Use this project to explore the basic relationship between transaction data, cryptographic hashes, and linked blocks.
