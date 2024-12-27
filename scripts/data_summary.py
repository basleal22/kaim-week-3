import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def col_data_summary(data):#check for variability for the numerical columns
    rows=[]
    numeric_column= data.select_dtypes(include=['int64','float64'])
    for column in numeric_column.columns:
        variability_metrics={'Columns':column,
                            'data standard_deviation':data[column].std(),
                            'data variance':data[column].var(),
                            'data mean':data[column].mean(),
    

                                   }
        rows.append(variability_metrics)
        summary_data=pd.DataFrame(rows)
    return summary_data

#check for datatype
def data_types(data):
    categorical_variables=data.select_dtypes(include=['object','category'])
    numerical_variables=data.select_dtypes(include=['int64','float64'])
    date_variables=data.select_dtypes(include=['datetime64'])
    bool_var=data.select_dtypes(include=['bool'])
    # Combine identified columns into a set
    return categorical_variables.columns.tolist(),numerical_variables.columns.tolist(), date_variables.columns.tolist(),bool_var.columns.tolist()
    