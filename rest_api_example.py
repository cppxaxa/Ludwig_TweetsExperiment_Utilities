from flask import Flask, request, jsonify # loading in Flask
from ludwig.api import LudwigModel # loading in Ludwig
import pandas as pd # loading pandas for reading csv

# creating a Flask application
app = Flask(__name__)

# Load the model
model = LudwigModel.load('results/experiment_run_0/model')

# creating predict url and only allowing post requests.
@app.route('/predict', methods=['GET'])
def predict():
    # Get data from Post request
    data = request.args.get('text')
    # Make prediction
    df = pd.DataFrame([data], columns=['text'])
    # making predictions
    pred = model.predict(data_df=df)
    print(pred)
    # returning the predictions as json
    return jsonify(pred['airline_sentiment_predictions'][0])

if __name__ == '__main__':
    app.run(port=3000, debug=True)

# http://127.0.0.1:3000/predict?text=i%20was%20served%20well