#!/usr/bin/env python

import pandas as pd

def main():
    '''
    Series dataset containing helpdesk employee names
    and # of closed tickets for month of October for that employee
    '''
    names = ['William', 'Alfred', 'Sarah']
    ticket_count = [126, 112, 242]

    # Closed ticket data series
    closed_tickets = pd.Series(ticket_count, index=names)

    # Dump contents of series to stdout
    print("Closed Tickets by Employee \n%s\n" % closed_tickets)

    # Calculate # of tickets closed per day 
    avg_tickets = closed_tickets.divide(other = 31)
    print("Average Tickets Closed per Day by Employee\n%s\n" % avg_tickets)

    # Number of closed tickets for an individual employee based on name
    print("Tickets closed by William: %s" % closed_tickets['William'])
    print("Tickets closed by Alfred: %s" % closed_tickets['Alfred'])
    print("Tickets closed by Sarah: %s" % closed_tickets['Sarah'])

if __name__ == "__main__":
    main()