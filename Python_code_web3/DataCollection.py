
import json



#put your own data here
msg_sender_address='0x38633BDD9205D0a26a70d0d84F2137f19785CC75'
private_key_of_account_file = open("../../private_key_of_account")
inp= json.load(private_key_of_account_file)
private_key_of_account=inp['key']

product_id=1
user_id=2
timestamp1=1605377851
timestamp2=9905377851

#private local Ethereum blockchain
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))

json_file = open("../build/contracts/DataCollection.json")
variables = json.load(json_file)
json_file.close()

myContract = w3.eth.contract(address=variables['networks']['5777']['address'], abi=variables['abi'])
#end of put your own data here





#write transaction examples
nonce = w3.eth.getTransactionCount(msg_sender_address)
transaction = myContract.functions.addDataCollected(
    product_id,user_id,"view",timestamp1).buildTransaction({
    'gas': 700000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'from': msg_sender_address,
    'nonce': nonce
    }) 
signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key_of_account)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)

nonce = w3.eth.getTransactionCount(msg_sender_address)
transaction = myContract.functions.addDataCollected(
    product_id,user_id,"view",timestamp2).buildTransaction({
    'gas': 700000,
    'gasPrice': w3.toWei('1', 'gwei'),
    'from': msg_sender_address,
    'nonce': nonce
    }) 

signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key_of_account)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)






#read transaction examples
count= myContract.functions.readDataCount(product_id,user_id).call()
print('Stored \'count\' in contract is:')
print(count)

for x in range(count):
	timestamp= myContract.functions.readDataTimestamp(product_id,user_id,x).call()
	print('Stored \'timestamp\' in contract is:')
	print(timestamp)


for x in range(count):
	datatype1= myContract.functions.readDataType(product_id,user_id,x).call()
	print('Stored \'type\' in contract is:')
	print(datatype1)


