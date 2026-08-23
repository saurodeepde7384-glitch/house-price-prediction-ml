import joblib
import pandas as pd

# Load model & scaler
model = joblib.load("house_price_model.pkl")


# User input
size = float(input("Enter house size (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Preprocess input

input_data = pd.DataFrame(
    [[size, bedrooms]],
    columns=["size_sqft", "bedrooms"]
)

# Predict
price = model.predict(input_data)

print(f"\nPredicted House Price: ₹{price[0]:,.0f}")
