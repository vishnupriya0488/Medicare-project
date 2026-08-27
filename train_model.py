import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.combine import SMOTEENN
import joblib

# Load dataset
df = pd.read_excel("MedicareFraud.xlsx")
print(df.head())

# Drop unnecessary columns
df.drop([
    'total_claim_amount',
    'police_report_available',
    'policy_number'
], axis=1, inplace=True, errors='ignore')

# 🔥 DROP ALL DATETIME COLUMNS
datetime_cols = df.select_dtypes(include=['datetime64[ns]']).columns
df.drop(datetime_cols, axis=1, inplace=True)

# Encode target
df['fraud_reported'] = df['fraud_reported'].map({'Y': 1, 'N': 0})

# Encode categorical columns safely
label_encoders = {}

for col in df.columns:
    if df[col].dtype == 'object' and col != 'fraud_reported':
        df[col] = df[col].astype(str)
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
df = df.apply(pd.to_numeric, errors='coerce')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)



# Split X & y
X = df.drop('fraud_reported', axis=1)
y = df['fraud_reported']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

X_train = X_train.fillna(0)
X_test = X_test.fillna(0)

# Handle imbalance
smote_enn = SMOTEENN(random_state=42)
X_resampled, y_resampled = smote_enn.fit_resample(X_train, y_train)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced'
)
model.fit(X_resampled, y_resampled)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model & encoders
joblib.dump(model, "fraud_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("✅ Model trained successfully without errors")
