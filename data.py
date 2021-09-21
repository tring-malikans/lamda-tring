# # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRyaW5nQHRyaW5nbGxjLmNvbSIsImlhdCI6MTYzMjAzNzc4MCwiZXhwIjo3OTM5MjM3NzgwfQ.CS-LohCdrLfMuR2Q4-7En0Gw5d_Ac6JNJRr6nylm8do

# Import the requests library 
# import requests 

# # Define indicator
# indicator = "tema"
  
# # Define endpoint 
# endpoint = f"https://api.taapi.io/{indicator}"
# my_secret="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRyaW5nQHRyaW5nbGxjLmNvbSIsImlhdCI6MTYzMjAzNzc4MCwiZXhwIjo3OTM5MjM3NzgwfQ.CS-LohCdrLfMuR2Q4-7En0Gw5d_Ac6JNJRr6nylm8do"
  
# # Define a parameters dict for the parameters to be sent to the API 
# parameters = {
#     'secret': my_secret,
#     'exchange': 'binance',
#     'symbol': 'BTC/USDT',
#     'interval': '1m',
#     'backtrack':9
#     } 
# parameters1 = {
#     'secret': my_secret,
#     'exchange': 'binance',
#     'symbol': 'BTC/USDT',
#     'interval': '1m',
#     'backtrack':20
#     } 
  
# # Send get request and save the response as response object 
# response = requests.get(url = endpoint, params = parameters)
# response1 = requests.get(url = endpoint, params = parameters1)
  
# # Extract data in json format 
# result = response.json() 
# result1 = response1.json() 

# # Print result
# print(result)
# print(result1)




# Import the requests library 
  
# Define endpoint 
# endpoint = "https://api.taapi.io/bulk"
# endpoint = "wss://ws.taapi.io"
# my_secret="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRyaW5nQHRyaW5nbGxjLmNvbSIsImlhdCI6MTYzMjAzNzc4MCwiZXhwIjo3OTM5MjM3NzgwfQ.CS-LohCdrLfMuR2Q4-7En0Gw5d_Ac6JNJRr6nylm8do"
# Define a JSON body with parameters to be sent to the API 
import json
import requests 
from websocket import create_connection

parameters = {
    "secret": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRyaW5nQHRyaW5nbGxjLmNvbSIsImlhdCI6MTYzMjA1MTk4OSwiZXhwIjo3OTM5MjUxOTg5fQ.Ma_-JXIchceqlcMpCt0q4af_g708_HBPF0XDXKUxbDc',
    "event":'subscribe',
    "data": [{
        "type":"crypto",
        "exchange": "binance",
        "symbol": "DOGE/BUSD",
        "interval": "5m",
        "indicators": [
	    {
                # Relative Strength Index
	        "indicator": "tema",
	    }
        ]
    }]
}
parameters1={
    "secret": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRyaW5nQHRyaW5nbGxjLmNvbSIsImlhdCI6MTYzMjA1MTk4OSwiZXhwIjo3OTM5MjUxOTg5fQ.Ma_-JXIchceqlcMpCt0q4af_g708_HBPF0XDXKUxbDc',
    "event":'unsubscribe'
}
            # 'backtrack':9
ws = create_connection("wss://ws.taapi.io")
ws.send(json.dumps(parameters))
result =  ws.recv()
print (result)
# ws.close()
# Send POST request and save the response as response object 
# response = requests.post(url = endpoint, json = parameters)
  
# Extract data in json format 
# result = response.json() 

# Print result
# print(result)