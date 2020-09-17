#!/usr/bin/env python

import pandas as pd

def return_data(filename):
    # Open CSV Data adn return a python dict after normalizing the data

    # Read in contents of the CSV file to the dataframe df
    df = pd.read_csv(filename)

    # Normalize data by removing leading and trailing spaces from strings inside df
    df = df.applymap(lambda x: x.strip() if isinstance(x,str) else x)

    # If a tenant_name is null(nan) drop the entire row(axis=0)
    df = df.dropna(axis=0, subset=['tenant_name'])

    # Normalize Bridge Domain and EPG values to uppercase
    df['bd_name'] = df['bd_name'].str.upper()
    df['epg_name'] = df['epg_name'].str.upper()

    # Drop duplicates
    df = df.drop_duplicates()

    # Convert df to python dictionary
    result = df.to_dict(orient='index')

    return result

