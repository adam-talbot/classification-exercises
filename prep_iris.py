import pandas as pd
from sklearn.model_selection import train_test_split

def clean_iris(df): # I will pass the unprepped df into the function
    """
    Cleans data in preparation for splitting
    """
    df.drop(columns = ['species_id'], inplace = True)
    df = df.rename(columns = {'species_name' : 'species'})
    df_dummy = pd.get_dummies(df['species'], drop_first=True)
    df = pd.concat([df, df_dummy], axis = 1)
    return df

def split_iris(df):
    """
    splits the data in train validate and test 
    """
    train_validate, test = train_test_split(df, test_size = 0.2, random_state = 123, stratify = df.species)
    train, validate = train_test_split(train_validate, test_size = 0.25, random_state = 123, stratify = train_validate.species)
    
    return train, validate, test

def prep_iris(df):
    """
    takes in a data from iris database, cleans the data, splits the data
    in train validate test 
    Returns three dataframes train, validate and test.
    """
    df = clean_iris(df)
    train, validate, test = split_iris(df)
    return train, validate, test