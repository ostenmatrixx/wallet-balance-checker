from web3 import Web3
from dotenv import load_dotenv
import os

# Load RPC URL from .env
load_dotenv()
RPC_URL = os.getenv("RPC_URL")
if not RPC_URL:
    raise Exception("❌ RPC_URL not found in .env")

# Connect to the blockchain
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    raise Exception("❌ Failed to connect to RPC")

# Load wallet addresses
with open("addresses.txt", "r") as f:
    addresses = [line.strip() for line in f if line.strip()]

# Ask user for token contract address
token_address_input = input("Enter token contract address (leave empty to check ETH balances): ").strip()

# If token address is provided, set up ERC-20 contract
if token_address_input:
    token_address = Web3.to_checksum_address(token_address_input)
    ERC20_ABI = [
        {
            "constant": True,
            "inputs": [{"name": "account", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "", "type": "uint256"}],
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "decimals",
            "outputs": [{"name": "", "type": "uint8"}],
            "type": "function",
        },
    ]
    token = w3.eth.contract(address=token_address, abi=ERC20_ABI)
    decimals = token.functions.decimals().call()
    print(f"✅ Token contract detected | Decimals: {decimals}\n")
else:
    print("✅ No token contract provided | Checking ETH balances instead\n")

# Function to check balances
def check_balance(address):
    try:
        checksum_address = Web3.to_checksum_address(address)
        if token_address_input:
            # ERC-20 balance
            balance = token.functions.balanceOf(checksum_address).call()
            human_balance = balance / (10 ** decimals)
            print(f"Wallet {checksum_address} has {human_balance} tokens")
        else:
            # ETH balance
            balance = w3.eth.get_balance(checksum_address)
            human_balance = w3.from_wei(balance, 'ether')
            print(f"Wallet {checksum_address} has {human_balance} ETH")
    except Exception as e:
        print(f"❌ Error with {address[:6]}...: {e}")

# Process all addresses
for addr in addresses:
    check_balance(addr)
