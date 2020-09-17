#!/usr/bin/env python

import pandas as pd
import numpy as np

def main():
    '''
    Create a DataFrame dataset containing hel desk empoloyee names and the
    number of closed tickets for the month of October for that employee in
    the network, server, and application queues.
    '''

    # Technician name list
    names = ['William', 'Alfred', 'Sarah']

    # Dictionary containing data
    helpdesk_data = {
        'network_tickets': [35, 12, 149],
        'server_tickets': [78, 95, 93],
        'app_tickets': [13, 5, np.nan]
    }

    # DataFrame using defined names as index and the helpdesk_data dict
    df = pd.DataFrame(helpdesk_data, index=names)

    # Dump the contents of the DataFrame df to stdout
    print("%s\n" % df)

    # Print info about the DataFrame to stdout
    print(df.info())

    # Replace null values with 0
    df = df.fillna(0)

    # Print minimum values for each column in the DataFrame to stdout
    print("\nMinimum Ticket Count by Type: \n%s\n" % df.min())

    # Print the mean values for each column in the DataFrame to stdout
    print("Mean Ticket Count by Type: \n%s\n" % df.mean())

    # Print num of closed tickets for an individual employee based on ticket type
    print("Network Tickets Closed by Employee:\n%s\n" % df['network_tickets'])
    print("Server Tickets Closed by Employee:\n%s\n" % df['server_tickets'])
    print("App Tickets Closed by Employee:\n%s\n" % df['app_tickets'])

    # Recast data type across DataFrame to convert all that were previously NaN values
    # This NAN fields converted to 0 will show up as a dtype of float64
    df = df.astype(int)

    # Reprint App Tickets to see different dtype
    print("App Tickets Closed by Employee:\n%s\n" % df['app_tickets'])

    # Add new column to df that is the sum of all tickets per employee
    df['closed_tickets'] = df['network_tickets'] + df['server_tickets'] + df['app_tickets']
    
    # Dump contents of df to see new column
    print("%s\n" % df)

    # Create a new series and then merge the series into the df
    # A df is a collection of series datasets
    job_role = pd.Series(['Systems Engineer', 'Systems Engineer', 'Network Engineer'], index=names, name='job_role')
    df = df.join(job_role)

    # Dump contents of df to see new column
    print("%s\n" % df)

if __name__ == "__main__":
    main()