from flask import Flask, request, jsonify
import joblib
import pickle
import sys


app = Flask(__name__)
# read classifier.ipynb exported to pipeline
classifier = joblib.load('./model.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json

    prediction = classifier.predict(json_['text']).tolist()
    print(prediction, file=sys.stderr)
    return jsonify({'prediction': prediction[0] })


if __name__ == '__main__':
    # classifier = joblib.load('./pipeline.pkl')
    app.run(
        port=5000,
        debug=True
    )