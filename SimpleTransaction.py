import hashlib


class Block:
    def __init__(self, previous_hash, transaction):
        self.transaction = transaction
        self.previous_hash = previous_hash
        string_to_hash = "".join(transaction) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()


blockchain = []

genesis_block = Block("Chancellor in the brink...", ["Satoshi sent 1 BTC to Ivan",
                                                     "Maria sent 3 BTC to Jenny",
                                                     "Satoshi sent 5 BTC to Hal Finey"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz",
                                                "John sent 5 BTC to Jenny"])

print("Block hash: Second Block")
print(second_block.block_hash)

third_block = Block(second_block.block_hash, ["A sent 2 BTC to B",
                                              "B sent 5 BTC to C"])

print("Block hash: Third Block")
print(third_block.block_hash)
