from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("./randomForest.pkl")

predictors = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
              'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',
              'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 
              'Amount']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    try:
        input_data = [data[p] for p in predictors]
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400
    
    input_data = np.array(input_data).reshape(1, -1)
    
    prediction = model.predict(input_data)
    
    return jsonify({"prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)