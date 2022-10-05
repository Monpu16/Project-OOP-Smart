import json

from web3 import Web3

#Importando librerias para compilar datos de contrato 
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()

with open(r"C:\Users\user\Documents\OOP_Project\web3py__simple__storage\SimpleStorage.sol" , "r") as file:
    simple_storage_file = file.read()

#Hacemos instalacion de la version de Solidity
print("Installing...")
install_solc("0.6.0")

# Codigo fuente del contraro implementando Solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

