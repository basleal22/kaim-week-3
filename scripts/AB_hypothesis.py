import pandas as pd
from scipy.stats import f_oneway,ttest_ind

def risk_across_province(data):
    """
    test to see if there are risk differences(total claims) across provinces
    using A/B hypothesis test: if it results in Null hypothesis according to our parameter,
                               then the conclusion will be that there is no difference
    """
    #step 1: organize (group by) province 
