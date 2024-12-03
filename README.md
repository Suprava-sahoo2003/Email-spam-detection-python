# Email-spam-detection-python
Email Spam Detection System using Machine Learning to classify emails as spam or ham, ensuring efficient and secure communication.



# Email Spam Detection System

A machine learning-based application for detecting and classifying emails as **spam** or **ham** (non-spam), ensuring secure and efficient email communication.

## Features
- Utilizes **Multinomial Naive Bayes** for text classification.
- Preprocessing techniques: tokenization, stopword removal, and stemming.
- Real-time spam detection through a Django-powered web application.
- Optimized for accuracy and performance.
- Software testing methodologies implemented for system reliability.

## Requirements
- Python 3.8 or above
- Django 4.0 or above
- Required Python libraries: 
  - `scikit-learn`
  - `pandas`
  - `numpy`
  - `nltk`
- Dataset: Public email datasets (e.g., Enron, SMS Spam Collection).

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Suprava-sahoo2003/Email-spam-detection-python.git]
Navigate to the project directory:
bash
Copy code
cd email-spam-detection
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run database migrations:
bash
Copy code
python manage.py migrate
Start the development server:
bash
Copy code
python manage.py runserver
Usage
Access the web app at http://127.0.0.1:8000.
Upload an email or input text to classify it as spam or ham.
Project Structure

Future Enhancements
Incorporate advanced machine learning models for higher accuracy.
Add support for multilingual email spam detection.
Implement hybrid classification approaches.



