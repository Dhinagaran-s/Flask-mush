from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
needColumn=pickle.load(open("ModelCreation/needColumn.pkl","rb"))
pipeline=pickle.load(open("ModelCreation/pipeline.pkl","rb"))
@app.route('/')
@app.route('/Home')
def homepage():
    return render_template('mainpage.html')

@app.route("/predict", methods=['POST', 'GET'])
@app.route("/predict")
def predict():
    if request.method == 'POST':
        
        
        all_column=needColumn.copy()
        all_column.insert(15,"veil-type")
        Gotvalues=[]
        for col in all_column:
            Gotvalues.append(request.form[col])
        Gotvalues.pop(15)
        val=pipeline.predict(np.array(Gotvalues).reshape(1,-1))
        result="Something Wrong!"
        if val[0]=='e':
            result="This mushroom is edible"
        else:
            result="This mushroom is poison"
        
        return  render_template('predict.html',r=result)
    else:
        return render_template("error.html")

if __name__ == "__main__":
    app.run(debug=True)