# Random data generator
# Jade Minwei Wang
# AI & Blockchain Hackathon 2020 Team GeniSys member

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

# https://www.recombee.com/
client = RecombeeClient('genisys-dev', "XQh1IuKiCWz417PjRWl9G0HgUf08yU8LbImH2ybVrfiwar8P0gTayZ78QimjAWuA")

import random
from datetime import datetime

data1=[]
data2=[]

def generate_data():
	DATA = []
	user_id = random.randrange(2,21)
	product_id = random.randrange(1,11)
	DATA.append(user_id)
	DATA.append(product_id)
	return DATA

for i in range(400):
	#print(generate_data())
	data1.append(generate_data())

for j in range(400):
	#print(generate_data())
	data2.append(generate_data())

#print(data1)
#print(data2)

for i in range(400):
	client.send(AddDetailView(data1[i][0], data1[i][1],
								cascade_create=True))
		client.send(AddPurchase(data2[i][0], data2[i][1],
								cascade_create=True))