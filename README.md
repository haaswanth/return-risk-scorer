# Return Risk Scorer

An end-to-end machine learning project that predicts the **return risk of an e-commerce order** and presents the prediction through an interactive **Streamlit web application**.

## 🚀 Live Demo

**Streamlit App:**
https://return-risk-scorerbymannemhaaswanth.streamlit.app/

## 📌 Project Overview

Product returns are an important challenge for e-commerce businesses because they can increase operational costs, reduce profitability, and create additional logistics and environmental impact.

This project uses machine learning to estimate the probability that an order may be returned. The predicted probability is converted into an easy-to-understand risk level:

* 🟢 **Low Risk**
* 🟡 **Medium Risk**
* 🔴 **High Risk**

The application allows users to enter order and customer-related information and receive an instant return-risk prediction.

## 🎯 Objectives

* Predict the likelihood of an order being returned.
* Build a classification model for return-risk prediction.
* Apply appropriate preprocessing and feature scaling.
* Evaluate the machine learning model.
* Convert prediction probability into understandable risk levels.
* Build an interactive Streamlit interface.
* Deploy the application for public access.

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data processing
* **Scikit-learn** – Machine learning
* **Joblib** – Saving and loading the trained model and scaler
* **Streamlit** – Web application and deployment
* **Jupyter Notebook** – Data analysis and model development

## 🤖 Machine Learning Model

The final model used in this project is:

**Random Forest Classifier**

The model was trained using the selected features after preprocessing and scaling.

The trained model is saved as:

```text
return_risk_model.pkl
```

The corresponding scaler is saved as:

```text
scaler.pkl
```

## 📊 Features Used

The model uses the following selected features:

```text
Product_Price
Order_Quantity
Discount_Applied
User_Age
Order_Value
year
month
day
Product_Category_Books
Product_Category_Clothing
Product_Category_Electronics
Product_Category_Toys
```

Categorical product categories were converted into numerical features during preprocessing.

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Standard Scaling
   ↓
Random Forest Model
   ↓
Model Evaluation
   ↓
Save Model + Scaler
   ↓
Streamlit Application
   ↓
Return Risk Prediction
```

## 📁 Project Structure

```text
return-risk-scorer/
│
├── app.py
├── notebook.ipynb
├── return_risk_model.pkl
├── scaler.pkl
├── requirements.txt
├── dataset.csv
└── README.md
```

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd return-risk-scorer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🌐 Deployment

The Streamlit application is deployed using **Streamlit Community Cloud**.

### Live Application

https://return-risk-scorerbymannemhaaswanth.streamlit.app/

## 📈 Output

The application provides:

* Predicted return probability
* Return-risk category
* User-friendly prediction results
* Interactive order input interface

## 🔮 Future Improvements

Possible future improvements include:

* Adding more customer behavioral features
* Improving model performance through hyperparameter tuning
* Adding explainable AI techniques
* Adding more detailed risk analysis
* Monitoring model performance with new data
* Adding business-cost-based decision recommendations
* Improving the dashboard with additional visualizations

## 👨‍💻 Project Development

This project was developed as a machine learning and deployment project, covering the workflow from data preprocessing and model development to Streamlit deployment.

**Development assistance:** ChatGPT was used as an AI assistant during the development process for guidance, debugging, explanations, code assistance, and project documentation.

## 📜 Disclaimer

This project is intended for educational and demonstration purposes. The predictions should not be considered guaranteed outcomes for real-world orders.

---

⭐ If you find this project useful, consider giving the repository a star!
