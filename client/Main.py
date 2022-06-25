import requests

with open('transactions.txt', 'r') as f:
    for line in f:
        print(line, end='\n')

url = 'http://localhost:5000/uploadedData'
transaction = {'transaction': line}


x = requests.post(url, json=transaction)
        
# ser.write("Data uploaded")
print("\nResponse received: "+x.text)
print("Data Uploaded")