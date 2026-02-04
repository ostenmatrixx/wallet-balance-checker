# Wallet Balance Checker

A simple Python script to check **ETH or ERC-20 token balances** for multiple wallets using a blockchain RPC URL. Safe and read-only — **no private keys needed**.  

---

## Features

- ✅ Check **ETH balances** for a list of wallet addresses.  
- ✅ Check **any ERC-20 token balance** by providing the token contract address.  
- ✅ Wallet addresses are read from a text file (`addresses.txt`).  
- ✅ RPC URL is stored securely in a `.env` file.  
- ✅ Auto-detects token decimals for correct balance formatting.  
- ✅ Prints results to the console.  
- ✅ Works on **EVM-compatible networks** (Ethereum, zkSync, Polygon, Arbitrum, Optimism, etc.).  

---

## Requirements

- Python 3.8+  
- `web3` library  
- `python-dotenv` library  

---
