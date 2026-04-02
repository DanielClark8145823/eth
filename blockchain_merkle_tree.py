import hashlib

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = [self.hash(tx) for tx in transactions]
        self.root = self.build_merkle_tree(self.transactions)

    @staticmethod
    def hash(data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_merkle_tree(self, nodes):
        if len(nodes) == 1:
            return nodes[0]
        
        new_level = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i+1] if i+1 < len(nodes) else left
            combined = self.hash(left + right)
            new_level.append(combined)
        return self.build_merkle_tree(new_level)

    def get_root(self):
        return self.root

if __name__ == "__main__":
    txs = ["转账0.5ETH", "转账1.2BTC", "转账500USDT", "投票提案"]
    mt = MerkleTree(txs)
    print("🌳 默克尔树构建完成")
    print(f"交易列表: {txs}")
    print(f"默克尔根: {mt.get_root()}")
