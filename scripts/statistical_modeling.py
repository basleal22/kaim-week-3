import pandas as pd
import numpy as np
#import tensorflow as tf
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForrestRegressor
def preprocess(data):
    categorical=[]
    numerical=[]
    for column in data.columns:
        if data[column].dtype == 'object':
            categorical.append(column)
        elif data[column].dtype in ['int64','float64']:
            numerical.append(column) 
    return numerical,categorical