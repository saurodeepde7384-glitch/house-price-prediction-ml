import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("house_data.csv")

# ----- PREPROCESSING -----

# 1. Handle missing values (fill with mean)
df["size_sqft"].fillna(df["size_sqft"].mean(), inplace=True)

# 2. Features & target
X = df[["size_sqft", "bedrooms"]]
y = df["price"]

# 3. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model & scaler
joblib.dump(model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained with basic preprocessing!")
