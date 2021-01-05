from flask import Flask, redirect, url_for, render_template, request, flash

import os
import json
import veryfi
import pprint
from random import randint

# api conf
client_id = "vrfOHDDnOc7blOlPtYKiKI1b0pdGffjzjRrgXZJ"
client_secret = "BchJJyLYIoek2N86921MS2GvLJCgdtckox5yMjB3s796IDHODFtKSrGa4XP0nOLoP5my81fWhl51PD4lRbDof7awWtZNsAxfFo8CEn603eL5SI9YfwTDZDy2G7LX4p39"
username = "hokejo5741"
api_key = "768fd6b5f23c7da36429610e691952b9"
client  = veryfi.Client(client_id,client_secret,username,api_key)


# app conf
app = Flask(__name__,template_folder='./')
app.secret_key = 'this is secret key'

PORT = int(os.environ.get('PORT', 5051))

app.config['invoice_upload'] = './Uploads'



@app.route('/',methods=['GET','POST'])
def index():
    try:
        message=""
        if request.method == 'POST':
            if request.files:
                try:
                    file = request.files['invoice']
                    print(file)
                    name_file = file.filename.split('.')
                    name_file= "{}{}.{}".format(name_file[0],randint(0,999),name_file[1])
                    print(name_file)
                    file.save(os.path.join(app.config['invoice_upload'],name_file))
                    categories = ['Invoice','Airfare','Travel','Lodging','Job Suplies and Materials','Grocery']
                    json_result  = client.process_document("Uploads/{}".format(name_file),categories)
                    pprint.pprint(json_result)
                    items = []
                    for i in json_result['line_items']:
                        items.append({
                            "sku":i['sku'],
                            "description":i['description'],
                            "qty":i['quantity'],
                            "uom":i['unit_of_measure'],
                            "total":i['total']
                        })
                    extracted_data = {
                        "issuer":json_result['vendor']['raw_name'],
                        "invoiceNumber":json_result['invoice_number'],
                        "date":json_result['date'],
                        "address":json_result['vendor']['address'],
                        "customer":json_result['bill_to_name'],
                        "customerAcc":json_result['account_number'],
                        "customerAddress":json_result['bill_to_address'],
                        "items":items,
                        "netTotal":json_result['subtotal'],
                        "taxAmmount":json_result['tax'],
                        "total":json_result['total']
                    }

                    json_file = open("app.json", "r")
                    data = json.load(json_file)
                    json_file.close()

                    data.append(extracted_data)

                    json_file = open("app.json", "w+")
                    json.dump(data,json_file)
                    json_file.close()
                    message="Extracted"
                    return redirect('/')
                except Exception as e:
                    return render_template("index.html",data=data,error=str(e))   
        else:
            with open("app.json") as json_file:
                data = json.load(json_file)
                return render_template("index.html",data=data,message=message)
    except Exception as e:
        flash(e)
        return render_template("index.html",error=str(e))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
