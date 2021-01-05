import veryfi
import pprint


client_id = "vrfOHDDnOc7blOlPtYKiKI1b0pdGffjzjRrgXZJ"
client_secret = "BchJJyLYIoek2N86921MS2GvLJCgdtckox5yMjB3s796IDHODFtKSrGa4XP0nOLoP5my81fWhl51PD4lRbDof7awWtZNsAxfFo8CEn603eL5SI9YfwTDZDy2G7LX4p39"
username = "hokejo5741"
api_key = "768fd6b5f23c7da36429610e691952b9"


client  = veryfi.Client(client_id,client_secret,username,api_key)

file  = open('extracted.txt','w+')
print('Starting Extarction.....')
print('processing file 1...')
categories = ['Invoice','Airfare','Travel','Lodging','Job Suplies and Materials','Grocery']
json_result  = client.process_document('Invoices/invoice.pdf',categories)
pprint.pprint(json_result)

file.write('===============Invoice 1===============\n')
file.write('Company Name: '+str(json_result['vendor']['raw_name'])+'\n')
file.write('Invoice Number: '+ str(json_result['invoice_number'])+'\n')
file.write('Address: '+ str(json_result['vendor']['address'])+'\n')
file.write('Date: '+ str(json_result['date'])+'\n')
file.write('Customer: '+ str(json_result['bill_to_name'])+'\n')
file.write('Customer A/C#: '+ str(json_result['account_number'])+'\n')
file.write('Customer Address: '+ str(json_result['bill_to_address'])+'\n')
file.write('=========List Items=========\n')
for i in json_result['line_items']:
    file.write('sku: '+ str(i['sku'])+'\n')
    file.write('qty: '+ str(i['quantity'])+'\n')
    file.write('description: '+ str(i['description'])+'\n')
    file.write('UOM: '+ str(i['unit_of_measure'])+'\n')
    file.write('total price: '+ str(i['total'])+'\n')

file.write('=========List Items End=========\n')

file.write('Net total: '+str(json_result['total'])+'\n')
file.write('======================================\n\n')

print('processing file 2...')
json_result1  = client.process_document('Invoices/default.pdf',categories)
# pprint.pprint(json_result1)
file.write('===============Invoice 2===============\n')
file.write('Company Name: Cetnaj\n')
file.write('Invoice Number: '+ str(json_result1['invoice_number'])+'\n')
file.write('Address: '+ str(json_result1['vendor']['address'])+'\n')
file.write('Date: '+ str(json_result1['date'])+'\n')
file.write('Customer: '+ str(json_result1['bill_to_name'])+'\n')
file.write('Customer A/C#: '+ str(json_result1['account_number'])+'\n')
file.write('Customer Address: '+ str(json_result1['bill_to_address'])+'\n')
file.write('=========List Items=========\n')
for i in json_result1['line_items']:
    file.write('sku: '+ str(i['sku'])+'\n')
    file.write('qty: '+ str(i['quantity'])+'\n')
    file.write('description: '+ str(i['description'])+'\n')
    file.write('UOM: '+ str(i['unit_of_measure'])+'\n')
    file.write('total price: '+ str(i['total'])+'\n')

file.write('=========List Items End=========\n')

file.write('Net total: '+str(json_result1['total'])+'\n')
file.write('======================================\n\n')

file.close()

print('extracted successfully result is in extracted.txt file')
