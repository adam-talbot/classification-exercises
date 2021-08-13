import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def clean_data(df):
    '''
    This function will drop any duplicate observations, 
    drop columns not needed,
    and create dummy vars of sex and embark_town. 
    '''
    df.drop_duplicates(inplace=True)
    df.drop(columns=['deck', 'embarked', 'class'], inplace=True)
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    return pd.concat([df, dummy_df], axis=1)


def split_data(df):
    """
    splits the data in train validate and test 
    """
    train, test = train_test_split(df, test_size = 0.2, random_state = 123, stratify = df.survived)
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.survived)
    
    return train, validate, test


def impute(train, validate, test):
    '''
    impute mode for embark_town
    '''
    imputer = SimpleImputer(strategy='most_frequent')
    train[['embark_town']] = imputer.fit_transform(train[['embark_town']])
    validate[['embark_town']] = imputer.transform(validate[['embark_town']])
    test[['embark_town']] = imputer.transform(test[['embark_town']])
    '''
    impute median for age
    '''
    imputer_age = SimpleImputer(strategy='median')
    train[['age']] = imputer_age.fit_transform(train[['age']])
    validate[['age']] = imputer_age.transform(validate[['age']])
    test[['age']] = imputer_age.transform(test[['age']])
    
    return train, validate, test


def prep_titanic_data(df):
    """
    takes in a data from titanic database, cleans the data, splits the data
    in train validate test and imputes the missing values for embark_town and age. 
    Returns three dataframes train, validate and test.
    """
    df = clean_data(df)
    train, validate, test = split_data(df)
    train, validate, test = impute(train, validate, test)
    return train, validate, test