from web3 import Web3

# 连接以太坊RPC节点
RPC_URL = "https://eth.llamarpc.com"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def get_eth_balance(address):
    # 校验地址格式
    if not w3.is_address(address):
        return "❌ 无效的以太坊地址"
    
    # 获取余额（Wei）并转换为ETH
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")
    
    print("="*50)
    print(f"🔗 连接状态: {'已连接' if w3.is_connected() else '连接失败'}")
    print(f"📌 查询地址: {address}")
    print(f"💰 ETH余额: {balance_eth:.6f} ETH")
    print("="*50)
    return balance_eth

if __name__ == "__main__":
    # 以太坊创世地址
    test_address = "0x0000000000000000000000000000000000000000"
    get_eth_balance(test_address)
