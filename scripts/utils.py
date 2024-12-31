import pandas as pd
import numpy as np
def feature_eng(data):
    data['claim_ratio']=data['TotalClaims']/data['TotalPremium']#helps capture efficiency or risk levels
    return data
#def one-hot-encoding(data);

