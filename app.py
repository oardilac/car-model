from flask import Flask, render_template, request
import jsonify
import requests
from datetime import date, datetime
import pickle
import numpy as np

app = Flask(__name__)

with open('modelFirst.pkl', 'rb') as f:
    model1 = pickle.load(f)

with open('modelSecond.pkl', 'rb') as f:
    model2 = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def prepare_data(request_form):
    year = int(request_form.get('year', datetime.now().year))
    present_price = float(request_form.get('present_price', 0))
    kms_driven = int(request_form.get('kms_driven', 0))
    kms_driven2 = np.log(kms_driven)
    owner = int(request_form.get('owner', 0))
    fuel_type_petrol = request_form.get('fuel_type_petrol', 'Petrol')
    seller_type_individual = request_form.get('seller_type_individual', 'Individual')
    transmission_manual = request_form.get('transmission_manual', 'Manual')
    
    year = datetime.now().year - year
    
    if fuel_type_petrol == 'Petrol':
        fuel_type_petrol = 1
        fuel_type_diesel = 0
    else:
        fuel_type_petrol = 0
        fuel_type_diesel = 1
    
    seller_type_individual = 1 if seller_type_individual == 'Individual' else 0
    transmission_manual = 1 if transmission_manual == 'Manual' else 0

    data = [present_price, kms_driven2, owner, year, fuel_type_diesel, fuel_type_petrol, seller_type_individual, transmission_manual]

    # Escala los datos de entrada utilizando el scaler cargado
    data_scaled = scaler.transform([data])  # Transforma los datos de entrada con el scaler

    return data_scaled[0]


@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = prepare_data(request.form)
        prediction1 = model1.predict([data])
        prediction2 = model2.predict([data])
        output1 = round(prediction1[0], 2)
        output2 = round(prediction2[0], 2)

        if output1 < 0 or output2 < 0:
            return render_template('index.html', prediction_texts='Lo sentimos, no puedes vender este carro')
        else:
            return render_template('index.html', prediction_text1=f'Precio 1: Puedes vender el carro a {output1}', 
                                   prediction_text2=f'Precio 2: Puedes vender el carro a {output2}')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)