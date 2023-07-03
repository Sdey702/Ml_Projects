from flask import request,render_template
from util.utils_Medicale_insurences import Medicale_insurences_util
from __main__ import app

# medicale insurence page
@app.route('/medicale_insurence')
def medicale_insurence():
    return render_template('medicale_insurence/medicale_insurence.html')


@app.route('/medical_insurence/predict_charges',methods = ['POST']) 
def predict_charges():

    data = request.form
    print("Data :",data)
    age      = data['age']
    gender   = data['gender']
    bmi      = data['bmi']
    children = data['children']
    smoker   = data['smoker']
    region   = data['region']

    print('*'*50,age,gender,bmi,children,smoker,region)

    # get predict value from utils class
    obj = Medicale_insurences_util(age,gender,bmi,children,smoker,region)
    pred_price = obj.get_predicted_price()
    
    return render_template("medicale_insurence/medicale_insurence_result.html",prediction=pred_price)

