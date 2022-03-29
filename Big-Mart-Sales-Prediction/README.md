# Big Mart Sales Prediction

Using the BigMart Sales Prediction data from Kaggle, a model is trained to forecast the sales of the products in the stores.
The model used is a Gradient Boosting Regressor. A pipeline is set up using sklearn and persisted as stored file using joblib.

The trained pipeline is then wrapped into an API using Flask. The API takes in either a CSV file (batch input) or an individual data record for inference.
