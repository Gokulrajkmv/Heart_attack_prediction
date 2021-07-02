import numpy as np
import pandas as pd
from flask import Flask, request,render_template
import pickle

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('Heart.html')

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 13) 
    loaded_model = pickle.load(open("heart_flask.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        result = ValuePredictor(to_predict_list)         
        if int(result)== 1: 
            prediction ='There is chance of Heart attack'
        else: 
            prediction ='no chance of Heart attack'            
        return render_template("result.html", prediction = prediction) 
if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
