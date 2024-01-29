# import requests
# import json
#
# base_url = 'http://127.0.0.1:8000'
#
# data_create = {
#     'date': '2024-02-01',
#     'customer_name': 'Test Customer'
# }
#
# headers = {'Content-Type': 'application/json'}
# response_create = requests.post(f'{base_url}/api/invoice/', data=json.dumps(data_create), headers=headers)
#
# # Check retrieval of data
# response_retrieve = requests.get(f'{base_url}/api/invoice/{response_create.json()["id"]}')
# print('Test Case 1 Response (Create):', response_create.json())
# print('Test Case 2 Response (Retrieve):', response_retrieve.json())

import requests
import json

base_url = 'http://127.0.0.1:8000'

# Test Case 1: Create an Invoice
data_create = {
    'date': '2024-02-01',
    'customer_name': 'Test Customer',
    'details': [
        {
            'description': 'Item 1',
            'quantity': 5,
            'unit_price': 10.50,
            'price': 52.50
        },
        {
            'description': 'Item 2',
            'quantity': 3,
            'unit_price': 15.75,
            'price': 47.25
        }
    ]
}

headers = {'Content-Type': 'application/json'}
response_create = requests.post(f'{base_url}/api/invoice/', data=json.dumps(data_create), headers=headers)

# Test Case 2: Retrieve the created Invoice
response_retrieve = requests.get(f'{base_url}/api/invoice/{response_create.json()["id"]}')
print('Test Case 1 Response (Create):', response_create.json())
print('Test Case 2 Response (Retrieve):', response_retrieve.json())
