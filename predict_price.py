import joblib
import pandas as pd

# Load model & scaler
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")

# User input
size = float(input("Enter house size (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Preprocess input

input_data = pd.DataFrame(
    [[size, bedrooms]],
    columns=["size_sqft", "bedrooms"]
)

input_scaled = scaler.transform(input_data)


# Predict
price = model.predict(input_scaled)

print(f"\n🏠 Predicted House Price: ₹{price[0]:,.0f}")
