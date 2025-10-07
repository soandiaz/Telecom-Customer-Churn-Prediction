# 📞 Telecom Customer Churn Prediction using Machine Learning

This project focuses on predicting whether a telecom customer will churn (discontinue the service) or not using **machine learning models**.
The workflow includes **data preprocessing and model building in Google Colab**, followed by **deployment using Streamlit** in PyCharm.

---

## 📊 **Dataset**

**Source:** [Kaggle - Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data)

* Type: Classification dataset
* Target variable: `Churn` (Yes / No)

---

## 🧱 **Project Structure**

```
Telecom-Customer-Churn-Prediction/
│
├── colab_code/                 
│   └── churn_model.ipynb     
│
├── requirements.txt
│
├── streamlit_app/          
│   ├── app.py           
│   └── assets/
│       └── global-connections.jpg
│
├── model/                        
│   ├── model.sav             
│   ├── scaler.sav                
│   └── label_encoder.sav               
│
├── dataset/                      
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
└── README.md                   
```

---

## 🧰 **Libraries Used**

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
mlxtend
xgboost
streamlit
pickle
```

---

## ⚙️ **Workflow**

### 🧪 1. Model Creation & Preprocessing (Colab)

* Imported and explored the dataset using Pandas and Seaborn.
* Cleaned data by removing irrelevant columns, handling null values, and converting categorical features using **LabelEncoder**.
* Identified class imbalance (`No: 5174`, `Yes: 1869`) and applied **undersampling** and **oversampling** techniques using `imblearn`.
* Conducted **feature selection** via correlation analysis and dropped less important columns.
* Created reusable functions for scaling, splitting, and training models.
* Trained multiple classifiers:

  * KNN Classifier
  * Support Vector Classifier (SVC)
  * Naive Bayes
  * Decision Tree
  * Random Forest
  * AdaBoost
  * Gradient Boosting
  * XGBoost
  * Logistic Regression
* Compared model performance and selected **XGBoost** as the best (Accuracy: **84%**).
* Built a **stacking ensemble** (base: XGBoost & Gradient Boosting; meta: Random Forest) — Accuracy: **83%**.
* Saved the trained model, encoder, and scaler using **Pickle**.

---

### 🌐 2. Deployment (Streamlit - PyCharm)

* Designed a clean two-page Streamlit web app:

  * **Page 1:** Takes user input (customer features).
  * **Page 2:** Displays prediction → *Customer will churn or not*.
* Implemented a custom background image using HTML/CSS styling.
* Loaded model, scaler, and encoder using Pickle for predictions.
* Packaged the app with `requirements.txt` for easy setup.

---

## 🧾 **Results**

| Model                    | Accuracy |
| ------------------------ | -------- |
| XGBoost                  | 84%      |
| Gradient Boosting        | 83%      |
| Random Forest            | 81%      |
| Stacking (XGB + GB + RF) | 83%      |

✅ **Best Performing Model:** XGBoost
✅ **Final Deployment:** Streamlit App

---

## 🚀 **How to Run the Project**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/<your-username>/Telecom-Customer-Churn-Prediction.git
cd Telecom-Customer-Churn-Prediction
```

### **2️⃣ Open and Explore Colab Notebook**

Open the `colab_code/churn_model.ipynb` file in Google Colab to view preprocessing and model training steps.

### **3️⃣ Run the Streamlit App**

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

### **4️⃣ Interact with the App**

* Enter customer details in the form.
* Get an instant prediction on whether the customer is likely to churn.

---

## 🧑‍🏫 **Mentor**

**Mentor:** *Dr.prajesha*

---

## 🏷️ **Tags**

`Machine Learning` `Data Science` `Python` `Streamlit` `XGBoost` `EDA` `Imbalanced Data` `Customer Churn` `Classification` `Colab` `AI`

---
