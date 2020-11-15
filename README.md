# TH0
# How to start

cd THO

Start ganache to run a private Ethereum blockchain
https://www.trufflesuite.com/docs/ganache/quickstart

Add/update your own "mnemonic" and "infura_link" in truffle-config.js file.

Execute the following two commands in the command prompt to compile and deploy the smart contract "DataCollection.sol" to the private Ethereum blockchain (ganache).
truffle compile
truffle migrate --reset

Add/update your own "msg_sender_address" and put the private key of your account into the "private_key_of_account_file" in /given_files/Server.py.

Add/update your own RecombeeClient account in /given_files/Server.py.

cd THO/given_files

Execute the following command in the command prompt
python3 Client.py

Execute the following command in another!!!!! command prompt
python3 Server.py
