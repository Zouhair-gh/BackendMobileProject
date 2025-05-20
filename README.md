AI Predict - Your Guide to Heart Disease Assessment

An intelligent multi-platform solution for early detection and prediction of heart disease using advanced machine learning techniques. This project integrates a web interface and mobile application to provide accessible and accurate predictions based on clinical parameters.

![ArchitectureProject](https://github.com/user-attachments/assets/2334511a-498c-4395-9f7b-e844166337cd)


 Overview

Heart disease remains one of the leading causes of mortality worldwide. Early detection and assessment can substantially improve outcomes and save lives. This project leverages machine learning algorithms to predict the likelihood of heart disease based on clinical and lifestyle parameters, making this vital health information more accessible through user-friendly web and mobile interfaces.

Features

- Cross-Platform Access: Available as both web application and Android mobile app
- Real-Time Prediction: Instant heart disease risk assessment based on clinical parameters
- User-Friendly Interface: Simple input forms with clear visualization of results
- High Accuracy Models: Implementation of machine learning algorithms optimized for heart disease prediction
- Secure API Communication: RESTful API handling secure data transfer between frontend and backend
 Technology Stack

 Backend
- Framework: Flask (Python)
- ML Models: Trained models saved as PKL files
- API: RESTful architecture for seamless communication with both platforms

 Web Application
- Frontend: HTML5, CSS3, JavaScript
- Visualization: Interactive graphs for displaying prediction results

 Mobile Application
- Platform: Android
- Language: Java
- Development Environment: Android Studio

 ML Models Implemented

The system uses a combination of several machine learning algorithms to ensure high accuracy in predictions:

- Random Forest Classifier
- Support Vector Machine (SVM)
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Neural Networks

 Quick Start

 Prerequisites
- Python 3.8 or higher
- Flask
- scikit-learn
- Android Studio (for mobile app development)
- Web browser (for web application)

 Installation

1. Clone the repository:
```bash
git clone [https://github.com/moradmarouane/heart-disease-prediction.git](https://github.com/Zouhair-gh/BackendMobileProject.git)

```

2. Set up the Flask backend:
```bash
cd backend
pip install -r requirements.txt
python app.py
```

3. Access the web application:
   - Navigate to 'http://localhost:5001' in your web browser

4. For the Android application:
   - Open the 'android' folder in Android Studio
   - Build and run the application on an emulator or physical device

 API Documentation

Endpoints

 POST /predict
Receives patient data and returns the heart disease prediction.

Request Body:
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

Response:
```json
{
  "prediction": 1,
  "probability": 0.85,
  "message": "High risk of heart disease detected"
}
```

Future Enhancements

- Integration with wearable devices for real-time health monitoring
- Implementation of additional machine learning models for improved accuracy
- Cloud deployment for wider accessibility
- Multi-language support
- User account system for tracking prediction history

Research Background

This implementation is based on research exploring the effectiveness of various machine learning techniques in predicting heart disease. The models were trained and validated using standardized medical datasets, achieving accuracy levels between 85-92% depending on the algorithm.
 License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

- Special thanks to the open-source community for the machine learning libraries
- Appreciation to the medical professionals who provided domain expertise during development
- Thanks to all contributors who have invested time and effort in improving this system



Disclaimer: This system is intended as a screening tool only and should not replace professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

Mobile version github link: "[https://github.com/Zouhair-gh/MobileBackend.git](https://github.com/MarouaneMorad/AI-PREDICT.git)"
