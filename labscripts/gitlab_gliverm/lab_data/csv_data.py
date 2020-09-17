#!/usr/bin/env python

from get_csv_data import return_data
from pprint import pprint

def main():
  # Generate the full path to the CSV file
  source_file = "/development/lab-1-master/data/aci_info.csv"

  # Parse the CSV file anda return a dict with the contents of the file
  result = return_data(source_file)

  # Dump the contents of dict
  pprint(result)

if __name__ == "__main__":
    main()
