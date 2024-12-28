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
    # Select numerical columns
    # Create a figure and axis for the plot
    plt.figure(figsize=(10, 6))
    # Plot the count of non-null values for each numerical column
    data[numerical_cols.columns].count().plot(kind='bar')
    # Add labels and title
    plt.xlabel('Column Names')
    plt.ylabel('Non-null Count')
    plt.title('Non-null Counts for Numerical Columns')
    # Show the plot
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    #plot bar charts for categorical columns
    # Get the value counts for the column
    category_counts = data[categorical_cols].value_counts()
    # Plot the distribution
    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
    plt.title(f'Distribution of {categorical_cols}', fontsize=16)
    plt.xlabel(f'{categorical_cols}', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()

def bivariate_analysis(data):
    plt.figure(figsize=(10,8))
    sns.scatterplot(data=data,x='TotalPremium',y='TotalClaims',hue='ZipCode',palette='viridis',alpha=0.7)
    plt.title('TotalPremium vs TotalClaims by ZipCode')
    plt.xlabel('TotalPremium')
    plt.ylabel('TotalClaims')
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',title='ZipCode')
    plt.show()
def correlation_matrix(data):
    correlation_data=data[['TotalPremium','TotalClaims']].corr()
    #plot the matrix
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_data,annot=True,cmap='coolwarm',fmt='.2f')
    plt.title("Correlation Matrix: TotalPremium and TotalClaims")
    plt.show()