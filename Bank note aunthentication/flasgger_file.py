# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:04:34 2022

@author: aadit
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_in=open('bankclassifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome all"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values

    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "hello the answer"+ str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """ Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
     - name: file
       in: formData
       type: file
       required: true
    
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))


if __name__=='__main__':
    app.run()
    