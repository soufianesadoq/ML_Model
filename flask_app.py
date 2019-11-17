import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle

# load model
model1 = pickle.load(open('knn_gewicht.pkl', 'rb'))
model2 = pickle.load(open('knn_uniform.pkl', 'rb'))

# app
app = Flask(__name__, template_folder='Template')

# routes
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',methods=['POST'])

@app.route('/prediction',methods=['POST','GET'])
def prediction():
    if request.method == 'POST':

        Temperatur = int(request.form['Temperatur'])
        relativeLuftfeuchtigkeit = int(request.form['relativeLuftfeuchtigkeit'])
        Niederschlag = int(request.form['Niederschlag'])
        Schnee = int(request.form['Schnee'])
        model = request.form['model']
        data = {'relative Luftfeuchtigkeit': [relativeLuftfeuchtigkeit], 'Temperatur': [Temperatur], 'Niederschlag': [Niederschlag], 'Schnee': [Schnee]}
        df = pd.DataFrame(data)
        print(type(model))
        print(np.array(data))
        if model == "1":
            pred = model1.predict(np.array(df))
            print(pred)
            return render_template('prediction.html', result=pred, model='gewichtes Model')

        if model == "2":
            pred = model2.predict(df)
            print(pred)
            return render_template('prediction.html', result=pred, model='Uniform Model')
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(port = 800, debug=True)
