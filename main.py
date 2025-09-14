import pandas as pd  # allow us to load in the csv file and work with it a lot eaiser
import csv
# its a module builtin  into python helps with dates and time in this project
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"  # this is a class variable assoiated with the class
    COLUMNS = ["date", "amount", "category", "description"]
    # intialized the CSV file we read to read the existing one or we have to create one

    @classmethod  # classmethod decorator. It will have the access to the class but not the instance. object oreinted programming
    def intialized_csv(cls):  # creating a class method
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # data frame is used acceess to load the data in the pandas from rows and columns
            df = pd.DataFrame(columns=cls.COLUMNS)
            # to export dataframe to csv file is
            df.to_csv(cls.CSV_FILE, index=False)
    # to add some entries in the method

    @classmethod
    def add_entry(cls, date, amount, category, description):
        # use pandas/CSV Writer to write in to the file
        # to write the new entry we have to create the new entry in the file
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }  # store in python dictionary
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # automatically close the file
            # a is pending to the end of the file. were just opening it and then putting cursor at the very end of the file.
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added succesfully")


# to run this we can use
CSV.intialized_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")
