📦 House Price Prediction using Machine Learning

A beginner-friendly Python machine learning project that predicts house prices based on features such as house size and number of bedrooms. This repository walks through data preprocessing, model training, model evaluation, and interactive prediction via the command line.

📌 Features

✔ Handles missing values
✔ Feature scaling using StandardScaler
✔ Linear Regression model for price prediction
✔ Clean preprocessing workflow
✔ Command-line based prediction tool
✔ Test/train split with evaluation metrics

📁 Project Structure
.
├── house_data.csv          # Dataset used for training
├── train_model.py          # Script to train and save the model
├── predict_price.py        # Script to predict price from user inputs
├── requirements.txt        # Dependencies
├── .gitignore              # Exclude environment and build files
└── README.md               # This file 😊

🧠 About the Project

This project demonstrates a typical machine learning workflow using Python and Scikit-Learn:

Load and visualize the dataset (house_data.csv)

Handle missing values

Train a regression model (Linear Regression)

Evaluate performance using metrics such as R-squared and Mean Absolute Error

Save the trained model

Load the model and make predictions from custom input

This helps understand the fundamentals of machine learning projects in a real-world context.

📦 Tech Stack

– Python
– Pandas
– NumPy
– Scikit-Learn
– JobLib (or Pickle)
– Command-line interface

🚀 Getting Started
📥 Clone the repository
git clone https://github.com/saurodeepde7384-glitch/house-price-prediction-ml.git
cd house-price-prediction-ml

🧰 Install dependencies

Using pip:

pip install -r requirements.txt

🧪 Train the Model

Before making predictions, train the model:

python train_model.py


This will:

✔ Load and preprocess the dataset
✔ Train a regression model
✔ Save the trained model locally

💡 Predict House Prices

After training, you can predict house prices using:

python predict_price.py


You’ll be prompted to enter:

House size (e.g., 1200)

Number of bedrooms (e.g., 3)

The script will return the predicted price based on the trained model.

📊 Example Usage

After training:

Enter house size (in sq. ft): 1600
Enter number of bedrooms: 3
Predicted price: $286,453 (example)

📈 Evaluation Metrics

Your model is evaluated using:

R² Score — measures how well predictions approximate actual values

MAE (Mean Absolute Error) — measures average absolute errors

These help you understand the performance and real accuracy of your model.

🤝 Contributing

Contributions are welcome! If you want to improve this project:

Fork the repo

Create a new branch

Make your changes

Submit a pull request

❓ Ideas for Improvements

Here are some suggestions to enhance this project:

✔ Add support for more features (location, age of house, etc.)
✔ Implement more advanced regression models (Random Forest, XGBoost)
✔ Add EDA notebook with visualizations
✔ Create a web app (Flask/FastAPI) for UI interface

📄 License

This project is open-source — feel free to reuse and adapt! (If you want a specific license like MIT or Apache, mention it here.)
