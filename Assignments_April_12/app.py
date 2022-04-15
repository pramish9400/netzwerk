import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify
import sklearn

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def results():
    Year = float(request.form['Year'])
    Present_Price = float(request.form['Present_Price'])
    Kms_Driven = float(request.form['Kms_Driven'])
    Transmission = float(request.form['Transmission'])
    Owner = float(request.form['Owner'])
    Fuel_Type_cat = float(request.form['Fuel_Type_cat'])
    Car_Name_cat = float(request.form['Car_Name_cat'])
    Seller_Type_cat = float(request.form['Seller_Type_cat'])



    x = np.array([[Year, Present_Price, Kms_Driven, Transmission, Owner, Fuel_Type_cat, Car_Name_cat, Seller_Type_cat]])
    model = pickle.load(open('model.pkl','rb'))
    Y_predict = model.predict(x)
    return jsonify({'Prediction': float(Y_predict)})


if __name__ == '__main__':
    app.run(debug = True, port = 1010)