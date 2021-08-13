import pandas as pd
import numpy as np
import os
from env import host, user, password

# 1. Make a function named get_titanic_data that returns the titanic data from the codeup data science database as a pandas data frame. 
# Obtain your data from the Codeup Data Science Database.

# def get_titanic_data():
#     from env import host, user, password # not sure if I should do this inside the function or outside
#     db = 'titanic_db'
#     url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
#     query = '''
#     select * from passengers;
#     '''
#     df = pd.read_sql(query, url)
#     return df

# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. 
# The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

# def get_iris_data():
#     from env import host, user, password # not sure if I should do this inside the function or outside
#     url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
#     query = '''
#     select * from measurements
#     join species using(species_id);
#     '''
#     df = pd.read_sql(query, url)
#     return df

# 3. Once you've got your get_titanic_data and get_iris_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for a local filename like titanic.csv or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

def get_titanic_data():
    
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        # read the SQL query into a dataframe
        url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
        query = '''
        select * from passengers;
        '''
        df = pd.read_sql(query, url)

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  
    
    
    
def get_iris_data():
    
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        # read the SQL query into a dataframe
        url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
        query = '''
        select * from measurements
        join species using(species_id);
        '''
        df = pd.read_sql(query, url)

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  