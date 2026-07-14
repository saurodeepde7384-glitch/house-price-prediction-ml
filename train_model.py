import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


# Load data
df = pd.read_csv("house_data.csv")

# ----- PREPROCESSING -----

# Features & target
X = df[["size_sqft", "bedrooms"]]
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#  Handling Missing Data Using Simple Imputer

imputer = SimpleImputer(strategy='mean')
X_train[['size_sqft']] = imputer.fit_transform(X_train[['size_sqft']])
X_test[['size_sqft']] = imputer.transform(X_test[['size_sqft']])

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model & scaler
joblib.dump(model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained with basic preprocessing!")
