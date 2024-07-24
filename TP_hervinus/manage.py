#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#from scripts.create_db import create_database_and_table
#from scripts.insert_data import insert_data
from analysis.regression import perform_regression

def main():
    create_database_and_table()
    insert_data()
    perform_regression()

#if __name__ == "__main__":
 #   main()