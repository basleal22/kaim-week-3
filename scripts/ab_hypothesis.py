import pandas as pd
from scipy.stats import f_oneway, ttest_ind
def test_risk_across_province(data):
    """Test if there are significant risk differences (Total Claims) across provinces.
        Null Hypothesis: There are no risk differences across provinces."""
    province_group=[data[data['Province']==p]['TotalClaims'] for p in data['Province'].unique()]
    result= f_oneway(*province_group)
    return {
        "test":"ANOVA",
        "Null Hypothesis": "No risk difference across provinces",
        "F-statistic" : result.statistic,
        "p-value" : result.pvalue,
        "Reject Null": result.pvalue < 0.05
    }
def test_risk_across_PostalCode(data):
    """test if there are significant risk differences (total claims) across PostalCode.
    Null hypothesis: there are no risk differences across provinces."""
    postal_group=[data[data['PostalCode']==p]['TotalClaims'] for p in data['PostalCode'].unique()]
    result = f_oneway(*postal_group)
    return {
        "test":"ANOVA",
        "Null Hypothesis": "No risk difference across postal code",
        "f-statistic" : result.statistic,
        "p-value": result.pvalue,
        'reject null':result.pvalue < 0.05
    }
def profit_difference_between_postal_codes(data):
    """test if there are significant profit differences across postalcode.
    Null hypothesis:there are no profit differences across postalcode."""
    data['margin']=data['TotalPremium']-data['TotalClaims']
    margin_postal = [data[data['PostalCode']==p]['margin']for p in data['PostalCode'].unique()]
    result = f_oneway(*margin_postal)
    return {
        "test" : "ANOVA",
        "Null Hypothesis" : "no profit differences across postalcode.",
        "f-statistic" : result.statistic,
        "p-value" : result.pvalue,
        "reject null": result.pvalue <0.05
    }
def risk_difference_Women_Men(data):
    """test if there are significant risk differences (total claims) between men and women.
    Null hypothesis: there are no risk differences between men and women."""
    male_group=data[data['Gender']=='Male']['TotalClaims']
    female_group = data[data['Gender']=='Female']['TotalClaims']
    result = ttest_ind(male_group,female_group,equal_var=False)
    return {
            "Test": "T-Test",
            "Null Hypothesis": "No significant risk differences between women and men",
            "T-Statistic": result.statistic,
            "p-Value": result.pvalue,
            "Reject Null": result.pvalue < 0.05
        }
