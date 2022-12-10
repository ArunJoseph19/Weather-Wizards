# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:27:56 2022

@author: A ARUN JOSEPHRAJ
"""

# importing Flask and other modules
from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
# Flask constructor
app = Flask(__name__)  

cols_to_use = ['sunHour', 'uvIndex', 'humidity','precipMM', 'visibility','pressure','FeelsLikeC']

def predict_DT(city,sunHour,uvIndex,humidity,precipMM,visibility,pressure):
    Dataset = 'Datasets/'+str(city)+'.csv'
    data = pd.read_csv(Dataset)
    X = data[cols_to_use[:-1]]
    y = data[cols_to_use[-1]]
    
    reg = DecisionTreeRegressor(max_depth=4)
    reg.fit(X, y)
    ft = [sunHour,uvIndex,humidity,precipMM,visibility,pressure]
    pred = reg.predict([ft])
    
    return round(pred[0],1)
 
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       city = request.form.get("city")
       sunHour = request.form.get("sunHour")
       uvIndex = request.form.get("uvIndex")
       humidity = request.form.get("humidity")
       precipMM = request.form.get("precipMM")
       visibility = request.form.get("visibility")
       pressure = request.form.get("pressure")
       print(city, sunHour,uvIndex,humidity,precipMM,visibility,pressure)
       return str(predict_DT(city, sunHour,uvIndex,humidity,precipMM,visibility,pressure))
    return render_template("index.html")
 
if __name__=='__main__':
   app.run()
   

#['sunHour', 'uvIndex', 'humidity','precipMM', 'visibility','pressure','FeelsLikeC']