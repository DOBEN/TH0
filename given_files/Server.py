# Recommendations server
# Adam Milton-Barker
# Doris Benda
# Blockchain & AI Hackathon 2020 Team GeniSys members

from flask import Flask, Response
from flask import request as frequest
import json
import jsonpickle
import requests as pyrequests
import time

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

from web3 import Web3

#put your own data here
deviceIp = "localhost"
serverPort = 9566

msg_sender_address='0x38633BDD9205D0a26a70d0d84F2137f19785CC75'
private_key_of_account_file = open("../../private_key_of_account")
inp = json.load(private_key_of_account_file)
private_key_of_account=inp['key']

#private local Ethereum blockchain
w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))

json_file = open("../build/contracts/DataCollection.json")
variables = json.load(json_file)
json_file.close()

myContract = w3.eth.contract(address=variables['networks']['5777']['address'], abi=variables['abi'])
#end of put your own data here

# Create account at https://www.recombee.com
client = RecombeeClient('genisys-dev', "XQh1IuKiCWz417PjRWl9G0HgUf08yU8LbImH2ybVrfiwar8P0gTayZ78QimjAWuA")

app = Flask(__name__)

@app.route('/Process', methods=['POST'])
def Process():
	""" Processes requests from GeniSys AI E-Commerce Magic Leap Application. """

	if frequest.headers["Content-Type"] == "application/json":
		query = frequest.json

		#send action to smart contract
		nonce = w3.eth.getTransactionCount(msg_sender_address)
		transaction = myContract.functions.addDataCollected(
			query["ProductID"], query["UserID"], query["Action"], int(time.time())).buildTransaction({
				'gas': 700000,
				'gasPrice': w3.toWei('1', 'gwei'),
				'from': msg_sender_address,
				'nonce': nonce
			})
		signed_txn = w3.eth.account.signTransaction(transaction, private_key=private_key_of_account)
		w3.eth.sendRawTransaction(signed_txn.rawTransaction)

		#count= myContract.functions.readDataCount(query["ProductID"],query["UserID"]).call()
		#print('Stored \'count\' in contract is:')
		#print(count)

		#for x in range(count):
			#datatype1= myContract.functions.readDataType(query["ProductID"],query["UserID"],x).call()
			#print('Stored \'type\' in contract is:')
			#print(datatype1)

		if query["Action"] == "View":
			#Send detail view to recommendation AI
			client.send(AddDetailView(query["UserID"], query["ProductID"], cascade_create=True))
		else:
			#Send purchase to recommendation AI
			client.send(AddPurchase(query["UserID"], query["ProductID"], cascade_create=True))

		#Get recommendation
		result = client.send(RecommendItemsToItem(query["ProductID"], query["UserID"], 5))

		return Response(response=json.dumps(result, indent=4, sort_keys=True), status=200, mimetype="application/json")
	else:
		return Response(response={}, status=405, mimetype="application/json")

def main():
	app.run(host=deviceIp, port=serverPort)

if __name__ == "__main__":
	main()
