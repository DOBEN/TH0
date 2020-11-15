# Recommendations test client
# Adam Milton-Barker
# Blockchain & AI Hackathon 2020 Team GeniSys members

import sys
import time
import string
import requests
import json
import random

#put your own data here
deviceIp = "localhost"
serverPort = 9566
#end of put your own data here

headers = {"content-type": 'application/json'}
url = "http://" + deviceIp + ":" + str(serverPort) + "/Process"

if __name__ == "__main__":

	response = requests.post(url, data=json.dumps({"UserID": random.randint(1,50), "Action": "View", "ProductID": 1}),
							headers=headers)
	print(response.text)
