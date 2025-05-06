from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load model and data
model = pickle.load(open("xgb.pkl", "rb"))
df = pd.read_csv("Cleaned_data.csv")

# Prepare dropdown options
areas = sorted(df["Area Name"].dropna().unique())
house_types = sorted(df["House Type"].dropna().unique())
furnishings = sorted(df["Furnishing"].dropna().unique())
years = sorted(df["Year Built"].dropna().unique())

# OneHotEncoder fitting (same structure as training)
categorical_features = ["Area Name", "House Type", "Furnishing"]
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoder.fit(df[categorical_features])

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html",
                           areas=areas,
                           house_types=house_types,
                           furnishings=furnishings,
                           years=years)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        area_name = data["area_name"]
        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])
        house_type = data["house_type"]
        furnishing = data["furnishing"]
        year_built = int(data["year_built"])

        input_df = pd.DataFrame({
            "Area Name": [area_name],
            "House Type": [house_type],
            "Furnishing": [furnishing]
        })

        encoded = encoder.transform(input_df)
        numeric = np.array([[area, bedrooms, bathrooms, year_built]])
        final_input = np.concatenate([encoded, numeric], axis=1)

        predicted_price = model.predict(final_input)[0]
        predicted_price = round(predicted_price)

        return jsonify({"predicted_price": predicted_price})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
