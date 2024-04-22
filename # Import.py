# Import necessary libraries
from flask import Flask, request, jsonify
import numpy as np
import pickle

# Create Flask app
app = Flask(__name__)

# Load the trained linear regression model
with open('graduation_prediction_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define route for prediction
@app.route('/predict_grads', methods=['POST'])
def predict():

    from flask import Flask

    app = Flask(__name__)

    # Get input data from request
    data = request.get_json()
    
    # Convert input data to numpy array
    input_data = np.array(data['input'])
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data.reshape(1, -1))
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction.tolist()})

# Define a basic route for testing
@app.route('/')
def index():
    return "Linear Regression Model Deployment with Flask"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
