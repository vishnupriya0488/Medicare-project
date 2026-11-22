# Medicare-project
# 🕵️ Medicare / Insurance Fraud Detection

A machine-learning web app that predicts whether an insurance claim is likely to be fraudulent. A Random Forest model is trained on historical claim data, and a Flask front end lets users enter claim details and see a prediction.

## 📌 Overview

Insurance fraud costs the industry billions each year. This project:

- Cleans and encodes a claims dataset (1,000 records, 39 features)
- Balances the heavily skewed classes using **SMOTEENN** (SMOTE + Edited Nearest Neighbours)
- Trains a **Random Forest** classifier
- Serves a simple **Flask** web interface for predictions

## 📂 Project Structure

```
├── MedicareFraud.xlsx      # Dataset
├── train_model.py          # Data preprocessing + model training
├── app.py                  # Flask web application
├── fraud_model.pkl         # Trained Random Forest model
├── label_encoders.pkl      # Saved LabelEncoders for categorical columns
└── templates/
    ├── index.html          # Input form
    └── result.html         # Prediction result page
```

## 📊 Dataset

`MedicareFraud.xlsx` contains **1,000 claims** and **39 columns**, including:

| Category | Example features |
|---|---|
| Policy | `policy_state`, `policy_csl`, `policy_deductable`, `policy_annual_premium`, `umbrella_limit` |
| Insured person | `age`, `insured_sex`, `insured_education_level`, `insured_occupation`, `insured_hobbies` |
| Incident | `incident_type`, `collision_type`, `incident_severity`, `incident_state`, `incident_hour_of_the_day` |
| Claim | `injury_claim`, `property_claim`, `vehicle_claim`, `total_claim_amount` |
| Vehicle | `auto_make`, `auto_model`, `auto_year` |
| **Target** | `fraud_reported` (Y / N) |

**Class distribution:** 753 non-fraud (N) vs. 247 fraud (Y), so the data is imbalanced (~75% / 25%).

## ⚙️ How It Works

1. **Load data** from `MedicareFraud.xlsx`.
2. **Drop** `total_claim_amount`, `police_report_available`, `policy_number` and all datetime columns.
3. **Encode** the target (`Y → 1`, `N → 0`) and label-encode categorical columns.
4. **Clean** the data: coerce to numeric, replace infinities, fill missing values with 0.
5. **Split** 80/20 into train/test (stratified, `random_state=42`).
6. **Balance** the training set with `SMOTEENN`.
7. **Train** `RandomForestClassifier(n_estimators=100, class_weight='balanced')`.
8. **Evaluate** with a classification report (precision, recall, F1).
9. **Save** the model and encoders with `joblib`.

## 🛠️ Tech Stack

- Python 3
- pandas, NumPy
- scikit-learn
- imbalanced-learn
- Flask
- joblib, openpyxl

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Install dependencies
```bash
pip install pandas numpy scikit-learn imbalanced-learn flask joblib openpyxl
```

### 3. Train the model
```bash
python train_model.py
```
This prints a classification report and creates `fraud_model.pkl` and `label_encoders.pkl`.

### 4. Run the web app
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser.


<img width="403" height="288" alt="image" src="https://github.com/user-attachments/assets/7a04fbc7-00b2-40e5-a605-dde692ef0db9" />


<img width="406" height="214" alt="image" src="https://github.com/user-attachments/assets/fe401ba0-e277-41ae-9b5e-a4c1d2f83dec" />

## 🖥️ Usage

1. Open the home page and fill in the claim details (claim amount, police report availability, policy number).
2. Click **Predict**.
3. The result page shows:
   - 🚨 **Fraud Reported**, or
   - ✅ **No Fraud Reported**

## ⚠️ Current Limitations

- The Flask app currently uses a **temporary rule-based check** (claim amount > 50,000 and no police report) instead of loading `fraud_model.pkl`. Integrating the trained model into `/predict` is the next step.
- The trained model expects the full feature set, while the web form collects only a few fields.
- The dataset is small (1,000 rows), so results may not generalize.

## 🔮 Future Improvements

- Connect `fraud_model.pkl` and `label_encoders.pkl` to the `/predict` route
- Expand the input form to cover the model's key features
- Add feature-importance visualizations
- Hyperparameter tuning and cross-validation
- Deploy to Render, Railway or Heroku

## 📄 License

This project is licensed under the MIT License.

## 👤 Author
**Vishnupriya**
[GitHub](https://github.com/vishnupriya0488) · [https://www.linkedin.com/in/vishnupriya-l-6544442a1)

