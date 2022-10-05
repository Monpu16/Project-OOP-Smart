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

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Obteniendo el Bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Obteniendo el Abi (Application Binary Interface)
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]

# Conectandonos a nuestro servidor en la Blockchain 
w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/a05b6ec2b4d94f56aea03fd3eb7256f1"))
chain_id = 5
my_address = "0x435D0CADBc8FC1904Dab96b394F11064D47BAcdc"
private_key = "0xfb29ef0b4fd6ca3d89ab118db776db9725573286adc6e62eb25ba690d5f9f8c1"

# Creando el contrato haciendo uso de Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# Obtener el numero del ultimo contrato 
nonce = w3.eth.getTransactionCount(my_address)
# Subir la transaccion que despliega nuestro contrato
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
# Firmando la transaccion 
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
# Enviando informacion del contrato 
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# Esperando a recibir confirmacion y recibo de la transaccion
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


# Trabajando con los contratos desplegados
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(f"Initial Stored Value {simple_storage.functions.retrieve().call()}")
greeting_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
    }
)
signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
print("Updating stored Value...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)

print(simple_storage.functions.retrieve().call())