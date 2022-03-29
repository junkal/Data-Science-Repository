
import os
import flask
import joblib
import json
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator

app = flask.Flask(__name__)
model = None

class OutletTypeEncoder(BaseEstimator):

    def __init__(self):
        pass

    def fit(self, documents, y=None):
        return self

    def transform(self, x_dataset):
        x_dataset['outlet_grocery_store'] = (x_dataset['Outlet_Type'] == 'Grocery Store')*1
        x_dataset['outlet_supermarket_3'] = (x_dataset['Outlet_Type'] == 'Supermarket Type3')*1
        x_dataset['outlet_identifier_OUT027'] = (x_dataset['Outlet_Identifier'] == 'OUT027')*1
        x_dataset['outlet_supermarket_1'] = (x_dataset['Outlet_Identifier'] == 'Supermarket Type1')*1

        return x_dataset

@app.route("/predict", methods=["POST"])
def predict():

    response = {"success": False}
    input = flask.request.files["data"].read().decode("utf-8")
    input = json.loads(input)

    mode = flask.request.files['mode'].read().decode("utf-8")

    if mode == "batch":
        predictions = model.predict(pd.DataFrame(input))
    elif mode == "single":
        predictions = model.predict(pd.DataFrame(input, index=[0]))
    else:
        return flask.jsonify(response)

    response["result"] = predictions.tolist()
    response["data_size"] = len(input)
    response["success"] = True

    return flask.jsonify(response)


if __name__ == '__main__':
    print("[INFO] *** Loading model and starting server..."
          "please wait until server has fully started ***")

    try:
        model = joblib.load('model.joblib')
    except FileNotFoundError as e:
        print(e)
        exit(1)

    print("[INFO] Remember to set environment variable ENV using: export ENV = local | webservice")

    environment = os.getenv('ENV')
    if environment == "local":
        print("ENV defined: local")
        app.run(host="127.0.0.1", port=4000, debug=True)
    elif environment == "webservice":
        print("ENV defined: webservice")
        app.run(host="0.0.0.0", port=4000, debug=True)
    else:
        print("[ERROR] Unknown environment, default to local IP")
        app.run(host="127.0.0.1", port=4000, debug=True)
