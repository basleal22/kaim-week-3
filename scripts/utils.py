from sklearn.preprocessing import train_test_split
from sklearn.ensemble import RandomForestRegressor
#from sklearn.decomposition import 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
def feature_eng(data):
    data['claim_ratio']=data['TotalClaims']/data['TotalPremium']#helps capture efficiency or risk levels
    return data
def missing_value(data):
    miss_value=data.fillna(0)
    return miss_value
def one_hot_encoding(data):
    low_cardinality_cols = ['Citizenship', 'LegalType', 'Title', 'Language', 'Bank', 'AccountType', 
    'Gender', 'Country', 'Province', 'MainCrestaZone', 'SubCrestaZone',
    'ItemType', 'VehicleType', 'AlarmImmobiliser', 'TrackingDevice', 
    'NewVehicle', 'CoverCategory', 'CoverType', 'CoverGroup', 'Section', 
    'Product', 'StatutoryClass', 'StatutoryRiskType']
    ordinal_cols = ['TermFrequency', 'ExcessSelected']

    # Apply one-hot encoding
    data = pd.get_dummies(data, columns=low_cardinality_cols, drop_first=True)
    high_cardinality_cols = ['make', 'Model', 'bodytype', 'VehicleIntroDate']

    for col in high_cardinality_cols:
        freq = data[col].value_counts() / len(data)
        data[col] = data[col].map(freq)
    # Label encoding for ordinal variables
    le = LabelEncoder()
    for col in ordinal_cols:
        data[col] = le.fit_transform(data[col])
    return data
def train_model(data):
    features = data.drop(columns=['TotalPremium', 'PolicyID', 'UnderwrittenCoverID', 'TransactionMonth'])
    target = data['claim_ratio']
    x= data[features]
    y=data[target]
    X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
    #data preprocessing
    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.transform(X_test)
    X_train=X_train.fillna(X_train.mean())
    X_test=X_test.fillna(X_test.mean())
    model_lr=LinearRegression()
    model_lr.fit(X_train_scaled,y_train)
    y_pred_lr= model_lr.predict(X_test_scaled)
    rf= RandomForestRegressor()
    rf.fit(X_train_scaled,y_train)
    y_pred_rf=model_lr.predict(X_test_scaled)
    from xgboost import XGBRegressor

    xgb = XGBRegressor(random_state=42)
    xgb.fit(X_train, y_train)
    y_pred_xgb = xgb.predict(X_test)
    return  y_pred_lr, y_pred_rf, y_pred_xgb
