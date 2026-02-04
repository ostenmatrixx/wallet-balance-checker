# Wallet Balance Checker

A simple Python script to check ETH or ERC-20 token balances for multiple wallets using a blockchain RPC URL. Safe and read-only — no private keys needed.

Features

✅ Check ETH balances for a list of wallet addresses.

✅ Check any ERC-20 token balance by providing the token contract address.

✅ Wallet addresses are read from a text file (addresses.txt).

✅ RPC URL is stored securely in a .env file.

✅ Auto-detects token decimals for correct balance formatting.

✅ Prints results to the console.

✅ Works on EVM-compatible networks (Ethereum, zkSync, Polygon, Arbitrum, Optimism, etc.).

Requirements

Python 3.8+

web3 library

python-dotenv library

Install dependencies using:

pip install web3 python-dotenv

Setup

Clone or download the project.

Create a .env file in the project folder and add your RPC URL:

RPC_URL=https://your-evm-rpc-url


⚠️ Important: The script only works on EVM-compatible networks. This includes Ethereum L1 and most L2s (zkSync, Arbitrum, Optimism, Polygon, etc.).
Simply input the correct RPC URL of the network where you want to check wallet balances.

Create addresses.txt with one wallet address per line:

0x1234...abcd
0xabcd...5678
0x5678...efgh

Usage

Run the script:

python check_balances.py


You will be prompted to enter a token contract address.

If left empty, the script will check ETH balances instead.

Example (ERC-20 token):

Enter token contract address (leave empty to check ETH balances):
0xDf70075737E9F96B078ab4461EeE3e055E061223


Output:

Wallet 0x1234...abcd has 150.25 tokens
Wallet 0xabcd...5678 has 0 tokens
Wallet 0x5678...efgh has 5.1 tokens


Example (ETH balance, leave blank):

Enter token contract address (leave empty to check ETH balances):

Wallet 0x1234...abcd has 0.75 ETH
Wallet 0xabcd...5678 has 0 ETH
Wallet 0x5678...efgh has 1.5 ETH

Security Notes

⚠️ Do NOT include private keys in this project. Only addresses are used.

RPC URL is stored in .env for safety.

The script only performs read-only calls — no transactions are sent.
