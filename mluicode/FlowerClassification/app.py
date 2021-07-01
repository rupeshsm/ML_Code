from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("iri.pkl", "rb"))

app = Flask(__name__)
cat = ["Setosa", "Versicolor", "Virginica"]
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/predict", methods = ["POST"])
def predict():
    #
    features=[ x for x in request.form.values()]
    final=[np.array(features)]
    pred = model.predict(final)
    print(features)
    final=int(pred)
    return render_template('predict.html', data=cat[final])





    
if __name__ == "__main__":
    app.run(debug=True)