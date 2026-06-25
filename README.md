# SMS Spam Detector

A machine learning-based web application built with Django that detects whether an SMS message is **Spam** or **Ham (Legitimate)**. The system uses a Naive Bayes classifier trained on an SMS Spam Collection dataset and provides a confidence score for predictions.

## Features

* SMS spam detection
* Naive Bayes classification
* Confidence score prediction
* Simple and user-friendly interface
* MySQL database integration

## Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Python, Django
* Database: MySQL
* Machine Learning: Naive Bayes, Scikit-learn
* Dataset: SMS Spam Collection Dataset

## How It Works

1. Enter an SMS message.
2. Click **Check Message**.
3. The trained model analyzes the text.
4. The application predicts whether the message is Spam or Ham.
5. A confidence score is displayed along with the result.

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/sms-spam-detector.git
cd sms-spam-detector

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```


## Author

Developed as part of an internship project using Django and Machine Learning.
