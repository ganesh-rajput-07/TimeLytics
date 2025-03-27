# Timelytics - Delivery Time Prediction

## 📌 Overview
Timelytics is a **Streamlit-based web application** that predicts the **delivery time** for customer orders based on various features such as product category, shipping method, and customer location. The application utilizes a **trained Random Forest model** to provide accurate delivery estimates.

## 🚀 Features
- **User Input Form**: Select product category, enter zip code, and choose shipping method.
- **Machine Learning Model**: Uses **Random Forest Regression** for prediction.
- **Interactive UI**: Built with Streamlit for an intuitive user experience.

## 📂 Dataset Used
The dataset consists of various features extracted from e-commerce transactions, including:
- **Product Category**
- **Customer Zip Code**
- **Shipping Method**
- **Purchase Date (Year, Month, Day)**
- **Actual Delivery Time**
- **Estimated Delivery Time**

## 🏗️ Tech Stack
- **Python** (Data Processing & Model Training)
- **Streamlit** (Frontend & Deployment)
- **Scikit-learn** (Random Forest Model)
- **Joblib** (Model Serialization)

## 🛠 Setup & Installation
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/ganesh-rajput-07/TimeLytics.git
cd timelytics
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```bash
streamlit run app.py
```

## 🎯 Model Training Process
The model was trained using:
1. **Preprocessed dataset** with relevant features.
2. **Train-test split** for model validation.
3. **Random Forest Regressor** for predicting delivery time.
4. **Evaluation metrics**: MAE, MSE, and R² score.

## 📈 Model Performance
- **Random Forest**
  - **Mean Absolute Error (MAE)**: 0.000477
  - **Mean Squared Error (MSE)**: 0.0030
  - **R² Score**: 0.9999
- **XGBoost (Alternative Model)**
  - **MAE**: 3.26
  - **MSE**: 21.19
  - **R² Score**: 0.68

## 📌 Future Improvements
- Optimize model for better generalization.
- Deploy online using **Streamlit Cloud** or **AWS/GCP**.
- Add **real-time tracking features** for better accuracy.

## 🤝 Contributing
Feel free to **fork** this repository, submit **pull requests**, or report **issues**!

## 📜 License
This project is licensed under the **MIT License**.

