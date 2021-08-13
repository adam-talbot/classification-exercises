import pandas as pd

def prep_iris(df): # I will pass the unpreped df into the function
    df.drop(columns = ['species_id'], inplace = True)
    df = df.rename(columns = {'species_name' : 'species'})
    df_dummy = pd.get_dummies(df['species'], drop_first=True)
    df = pd.concat([df, df_dummy], axis = 1)
    return df