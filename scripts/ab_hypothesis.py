import pandas as pd
from scipy.stats import f_oneway,ttest_ind

def risk_across_province(data):
    """
    test to see if there are risk differences(total claims) across provinces
    using A/B hypothesis test: if it results in Null hypothesis according to our parameter,
                               then the conclusion will be that there is no difference
    """
    #step 1: organize (group by) province 
    province_groups=[data[data['Province']==p]['TotalClaims'] for p in data['Province'].unique()]
    #step 2: use anova method to return the p values and statistics(with the f_oneway method)
    results = f_oneway(*province_groups)
    #step 3: return a dictionary of values having test type, pvalue, f-statistics 
    return {"test":"ANOVA",
            "Null Hypothesis":"No risk difference across provinces",
            "p-value":results.pvalue,
            "f-statistics":results.statistic,
            "reject null":results.pvalue < 0.05
            }
def risk_between_postalcodes(data):
    """
    test to see if there are risk differences(Total claims) across postalcodes
    using A/B hypothesis test: if it results in Null hypothesis according to our parameter,
                               then the conclusion will be that there is no difference
    """
    #step 1: organize (group by) postal code
    postalcode_groups=[data[data['PostalCode']==po]['TotalClaims'] for po in data['PostalCode'].unique()]#using unique so that we want to filter redundant postalcode values
    #step 2: use anova method to return the p values and statistics
    results = f_oneway(*postalcode_groups)
    #step 3: return a disctionary of values having test type, pvalue, f-statistics...
    return {"test":"ANOVA",
            "Null Hypothesis":"No risk difference across PostalCodes",
            "p-value":results.pvalue,
            "f-statistics":results.statistic,
            "reject null":results.pvalue < 0.05
            }
def marigin_between_postalcode(data):
    """
    test to see if there are margin differences(profit) across postalcodes
    using A/B hypothesis test: if it results in Null hypothesis according to our parameter,
                               then the conclusion will be that there is no difference
    """
    #step 1: create a marigin(our profit) column by subtracting premium to totalclaim
    data['Margin']=data['TotalPremium']-data['TotalClaims']
    #step 2: organize (group by) postal code
    postalcode_groups=[data[data['PostalCode']==po]['Margin'] for po in data['PostalCode'].unique()]#using unique so that we want to filter redundant postalcode values
    #step 3: use anova method to return the p values and statistics
    results = f_oneway(*postalcode_groups)
    #step 4: return a dictionary of values having test type, pvalue, f-statistics...
    return {"test":"ANOVA",
            "Null Hypothesis":"No profit difference across PostalCodes",
            "p-value":results.pvalue,
            "f-statistics":results.statistic,
            "reject null":results.pvalue < 0.05
            }
def risk_across_gender(data):
     
     """
    test to see if there are risk differences(totalclaims) across gender
    using A/B hypothesis test: if it results in Null hypothesis according to our parameter,
                               then the conclusion will be that there is no difference
    """
    #step 1: create male and female groups from the gender column
     male_group=data[data['Gender']=='Male']['TotalClaims']
     female_group=data[data['Gender']=='Female']['TotalClaims']
     #step 2: use anova method(ttest_ind) to compare the mean between the two datas(total claims)
     results = ttest_ind(male_group,female_group, equal_var=False)
     #step 3: return a dictionary of values having test type, pvalue, f-statistics...
     return {"test":"ANOVA",
            "Null Hypothesis":"No profit difference across PostalCodes",
            "p-value":results.pvalue,
            "f-statistics":results.statistic,
            "reject null":results.pvalue < 0.05
            }
    

