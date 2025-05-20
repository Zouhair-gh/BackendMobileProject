from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = pickle.load(open("./PKLs/RF.pkl", "rb"))

def getParameters():
    age = request.args.get('age')
    sex = request.args.get('sex')
    cp = request.args.get('cp')
    trestbps = request.args.get('trestbps')
    chol = request.args.get('chol')
    fbs = request.args.get('fbs')
    restecg = request.args.get('restecg')
    thalach = request.args.get('thalach')
    exang = request.args.get('exang')
    oldpeak = request.args.get('oldpeak')
    slope = request.args.get('slope')
    ca = request.args.get('ca')
    thal = request.args.get('thal')
    
    params = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    return (params)

@app.route('/')
def index():
    return render_template('y_index.html')
 
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])
        
        user_input = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        
        prediction = model.predict(user_input)
    
        if prediction[0] == 1:
            result = "Likely to have Heart Disease"
        else:
            result = "Not likely to have Heart Disease"
        
        data = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal,
            'result': result
        }
        
        return render_template('results.html', data=data)

@app.route('/predict1', methods=['POST', 'OPTIONS'])  
def predict1():
  
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        return response
        
    if request.method == 'POST':
        try:
            print("Received POST request:", request.data)  
            data = request.get_json()
            
            if not data:
                return jsonify({'error': 'No JSON data received'}), 400
                
            print("Request data:", data) 
            
            required_fields = [
                'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
            ]
            
            for field in required_fields:
                if field not in data:
                    return jsonify({'error': f'Missing required field: {field}'}), 400
            
            age = float(data['age'])
            sex = float(data['sex'])
            cp = float(data['cp'])
            trestbps = float(data['trestbps'])
            chol = float(data['chol'])
            fbs = float(data['fbs'])
            restecg = float(data['restecg'])
            thalach = float(data['thalach'])
            exang = float(data['exang'])
            oldpeak = float(data['oldpeak'])
            slope = float(data['slope'])
            ca = float(data['ca'])
            thal = float(data['thal'])
            
            if not (0 < age <= 120):
                return jsonify({'error': 'Age must be between 0 and 120'}), 400
            if sex not in [0, 1]:
                return jsonify({'error': 'Sex must be 0 (female) or 1 (male)'}), 400
            
            user_input = np.array([[
                age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                exang, oldpeak, slope, ca, thal
            ]])
            
            prediction = model.predict(user_input)
            prediction_proba = model.predict_proba(user_input)  
            
        
            response = {
                'prediction': int(prediction[0]),
                'result': "Likely to have Heart Disease" if prediction[0] == 1 
                          else "Not likely to have Heart Disease",
                'probability': float(prediction_proba[0][1]), 
                'parameters': {
                    'age': age,
                    'sex': sex,
                    'cp': cp,
                    'trestbps': trestbps,
                    'chol': chol,
                    'fbs': fbs,
                    'restecg': restecg,
                    'thalach': thalach,
                    'exang': exang,
                    'oldpeak': oldpeak,
                    'slope': slope,
                    'ca': ca,
                    'thal': thal
                }
            }
            
            print("Sending response:", response)  
            return jsonify(response)
            
        except ValueError as ve:
            print("ValueError:", str(ve))  
            return jsonify({'error': f'Invalid parameter value: {str(ve)}'}), 400
        except KeyError as ke:
            print("KeyError:", str(ke))  
            return jsonify({'error': f'Missing required parameter: {str(ke)}'}), 400
        except Exception as e:
            print("Exception:", str(e)) 
            return jsonify({'error': f'Server error: {str(e)}'}), 500
    

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5001, debug=True) 