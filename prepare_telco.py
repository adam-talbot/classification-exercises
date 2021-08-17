import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def clean_telco(df):
    df.drop(columns = ['payment_type_id', 'contract_type_id', 'internet_service_type_id', 'customer_id'], inplace=True)
    df.total_charges.replace(to_replace={' ' : '0'}, inplace = True)
    df.total_charges = df.total_charges.astype('float')
    df.senior_citizen = np.where(df.senior_citizen == 1, 'Yes', 'No')
    return df

def dummy_and_split(df):
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    dummy_df = pd.get_dummies(df[cat_cols], drop_first = True)
    df_w_dummies = pd.concat([df, dummy_df], axis=1)
    # df_w_dummies.drop(columns=cat_cols, inplace=True)
    train, test = train_test_split(df_w_dummies, test_size=.2, random_state=123, stratify=df_w_dummies.churn_Yes)
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train.churn_Yes)
    return train, validate, test

def prepare_telco(df):
    df = clean_telco(df)
    train, validate, test = dummy_and_split(df)
    return train, validate, test