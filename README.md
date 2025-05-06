# 🏠 Lahore House Price Predictor

This is a machine learning web application built with Flask that predicts house prices in Lahore. It uses an XGBoost model trained on custom data and a clean frontend with HTML, CSS, and JavaScript.

---

## 📌 Features

- Trained XGBoost model for regression
- OneHotEncoding on categorical columns
- Flask backend for prediction API
- Responsive frontend with dark mode
- Custom logo and design
- Deployed on Render

---

## 🧠 Model Info

- Model: XGBoost Regressor
- Preprocessing: OneHotEncoder
- Trained on custom housing data
- Saved as: `xgb.pkl`

---

## 📂 Dataset

- Created manually and cleaned
- Columns used:
  - Area Name (categorical)
  - House Type (categorical)
  - Furnishing (categorical)
  - Area (numeric)
  - Bedrooms (numeric)
  - Bathrooms (numeric)
  - Year Built (numeric)

---

## 🚀 How to Run Locally

1. Clone the repo
```bash
git clone https://github.com/your-username/lahore-house-price-predictor.git
cd lahore-house-price-predictor
Install packages

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open in browser:

arduino
Copy
Edit
http://localhost:5000/
🖼 UI
Dropdowns: Area Name, House Type, Furnishing

Inputs: Area (Marla), Bedrooms, Bathrooms, Year Built

Submit button to get predicted price

Logo on top

Dark mode toggle

Mobile responsive layout

🌐 Deployment
Hosted on Render.com

Requirements:

pip install -r requirements.txt

Start command: python app.py

👨‍💻 Developer
Ali Ahmad

Software Engineering Student

The Islamia University of Bahawalpur

Passionate about ML & Web Development

📁 Project Structure
cpp
Copy
Edit
📦 lahore-house-price-predictor
├── app.py
├── xgb.pkl
├── Cleaned_data.csv
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── logo.png
└── README.md
