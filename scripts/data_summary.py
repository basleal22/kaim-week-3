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
    # Sampling the data for visualization
    sampled_data = data.sample(100000, random_state=42)  # Sample 10,000 rows

    # Create a figure for the plot
    plt.figure(figsize=(10, 6))

    # Plot the count of non-null values for each categorical column
    categorical_cols.notnull().sum().plot(kind='bar', color='skyblue')

    # Add labels and title
    plt.xlabel('Column Names')
    plt.ylabel('Non-null Count')
    plt.title('Non-null Counts for Categorical Columns')

    # Adjust the x-axis for better readability
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Show the plot
    plt.show()

def bivariate_analysis(data):
    plt.figure(figsize=(10,8))
    sns.scatterplot(data=data,x='TotalPremium',y='TotalClaims',hue='Country',palette='viridis',alpha=0.7)
    plt.title('TotalPremium vs TotalClaims by Country')
    plt.xlabel('TotalPremium')
    plt.ylabel('TotalClaims')
    plt.legend(bbox_to_anchor=(1.05,1),loc='upper left',title='Country')
    plt.show()
def correlation_matrix(data):
    correlation_data=data[['TotalPremium','TotalClaims']].corr()
    #plot the matrix
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_data,annot=True,cmap='coolwarm',fmt='.2f')
    plt.title("Correlation Matrix: TotalPremium and TotalClaims")
    plt.show()
def data_comparision(data):
    # Aggregating data by ZipCode or geographical column
    geo_col = 'Country' 
    columns_to_compare = ['CoverType', 'TotalPremium', 'make']  

    # Create a summarized dataset
    geo_summary = data.groupby(geo_col)[columns_to_compare].agg(
    {
        'CoverType': lambda x: x.mode()[0] if not x.mode().empty else None,  # Most common CoverType
        'TotalPremium': 'mean',  # Average premium
        'make': lambda x: x.mode()[0] if not x.mode().empty else None  # Most common auto make
    }).reset_index()
    # Plotting Average TotalPremium by Country
    plt.figure(figsize=(16, 6))
    sns.barplot(x=geo_summary[geo_col], y=geo_summary['TotalPremium'], palette='coolwarm')

    plt.title('Average TotalPremium by Country', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Average TotalPremium', fontsize=14)
    plt.xticks(rotation=45)
    plt.show()
def outliers_detection(data):
    outliers_dict={}
    numerical_columns=data.select_dtypes(include=['int64','float64'])
    for cols in numerical_columns.columns:
        Q1=np.percentile(data[cols],25)
        Q3=np.percentile(data[cols],75)
        IQR=Q3-Q1
        #calculate bounds
        lower_bound=Q1-1.5*IQR
        upper_bound=Q3+1.5*IQR
        outliers = data[cols][(data[cols] < lower_bound) | (data[cols] > upper_bound)]
        outliers_dict[cols] = outliers
        outliers_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in outliers_dict.items()]))
    # Plot box plots
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=outliers_df, palette="Set2", width=0.5)

    # Add labels and title
    plt.title("Box Plot with Outliers Across Numerical Columns", fontsize=16)
    plt.xlabel("Columns", fontsize=14)
    plt.ylabel("Values", fontsize=14)

    # Show the plot
    plt.xticks(rotation=45)  # Rotate column names for readability
    plt.tight_layout()
    plt.show()