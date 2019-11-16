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
def index():
    return render_template('home.html',methods=['POST'])
##@app.route('/home', methods=['GET','POST'])
#def predict():
    # get data
 #   data = request.get_json(force=True)
  #  if request.method == 'POST':
   #     data = request.form.get(data)
    #    data_df = pd.DataFrame(data)
     #   erg = model1.predict(data_df)
      #  print(erg)
       # return render_template('home.html', perediction = erg[0])
    # convert data into dataframe
    #data.update((x, [y]) for x, y in data.items())
    #data_df = pd.DataFrame.from_dict(data)

    # predictions
    #result = model.predict(data_df)

    # send back to browser
    #print(result)
    #return render_template('index.html', sentiment=result['airline_sentiment_predictions'][0])

    # return data
    #return jsonify(results=output)
    #if request.method == 'POST':
     #   data = request.form.get('text')
        # Make prediction
      #  df = pd.DataFrame([str(data)], columns=['content'])
       # print(df.head())
        #pred = model.predict(data_df=df)
        #print(pred)
        #return render_template('index.html', sentiment=pred['airline_sentiment_predictions'][0])
    #return render_template('index.html', sentiment='')
@app.route('/prediction',methods=['POST'])
def prediction():
    if request.method == 'POST':

        Temperatur = request.form['Temperatur']
        relativeLuftfeuchtigkeit = request.form['relativeLuftfeuchtigkeit']
        Niederschlag = request.form['Niederschlag']
        Schnee = request.form['Schnee']
        model = request.form['model']
        data = {'Temperatur': [Temperatur], 'relative Luftfeuchtigkeit': [relativeLuftfeuchtigkeit], 'Niederschlag': [Niederschlag], 'Schnee': [Schnee]}
        df = pd.DataFrame(data)
        print(model)
        print(pd.DataFrame(data))
        if model == 1:
            pred = model1.predict(df)
            print(pred)
            return render_template('prediction.html' , result = pred , model = 'gewichtes Model')

        if model == 2:
            pred = model2.predict(df)
            print(pred)
            return render_template('prediction.html' , result = pred , model = 'Uniform Model')
    return render_template('home.html')
if __name__ == '__main__':
    app.run(port = 800, debug=True)
