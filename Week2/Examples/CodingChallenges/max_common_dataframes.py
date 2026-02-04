#https://www.codewars.com/kata/5ea2a798f9632c0032659a75
import pandas as pd
import numpy as np

def max_common(df1, df2):
    """
    Return a DataFrame with df1's structure, but with max values for common columns.
    
    Args:
        df1: First pandas DataFrame
        df2: Second pandas DataFrame
    
    Returns:
        New DataFrame with df1's columns, using max values from common columns
    """
    # Create a copy to avoid modifying the original
    result = df1.copy()
    
    # Find common columns
    common_cols = df1.columns.intersection(df2.columns)
    
    # For each common column, take the maximum value
    for col in common_cols:
        result[col] = np.maximum(df1[col], df2[col])
    
    return result

df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))
#df_out = pd.DataFrame(data=[[2.5, 6.0, 2.0], [2.0, 2.0, 8.5]], columns=list('ABC'))

print(max_common(df_a,df_b))