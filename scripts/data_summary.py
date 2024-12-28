import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
def missing_values_handle(data):
    title_to_gender={'Mr':'Male',
                     'Mrs':'Female',
                     'Ms':'Female',
                     'Miss':'Female',
                     }
    numerical_cols=data.select_dtypes(include=['int64','float64']).columns
    categorical_cols=data.select_dtypes(include=['object','category']).columns
    for column in data.columns:
        if column in numerical_cols:
            data[column]=data[column].fillna(data[column].mean())
        if column == 'Gender':
            data['Gender']=data['Gender'].fillna(data['Title'].map(title_to_gender))
        if column in categorical_cols:
            data.fillna(data[column].mode().iloc[0])
    return data

def num_cat_visual(data):
    #perform univariate analysis on the numerical and categorial columns
    categorical_cols=data.select_dtypes(include=['object','category'])
    numerical_cols=data.select_dtypes(include=['int64','float64'])
    #plot histogram for numerical columns
    plt.figure(figsize=(10,8))
    for col in numerical_cols:
        sns.histplot(data[col],kde=True,color='blue')
    plt.title(f'distribution solumns')
    plt.xlabel(col)
    plt.ylabel('frequency')
    plt.show()
    #plot bar charts for categorical columns
    plt.figure(figsize=(8,6))
    for col in categorical_cols:
        data[col].value_counts().plot(kind='bar',color= 'green')#Use the value_counts() method to calculate the frequency of each category.
    plt.title(f'distribution of columns')
    plt.xlabel('columns')
    plt.ylabel('count')
    plt.show()
def bivariate_analysis(data):
    plt.figure(figsize=(10,8))
    sns.scatterplot(data=data,x='TotalPremium',y='TotalClaims',hue='ZipCode',palette='viridis',alpha=0.7)
    plt.title('TotalPremium vs TotalClaims by ZipCode')
    plt.xlabel('TotalPremium')
    plt.ylabel('TotalClaims')
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',title='ZipCode')
    plt.show()