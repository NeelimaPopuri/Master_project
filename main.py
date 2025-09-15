import pandas as pd  # allow us to load in the csv file and work with it a lot eaiser
import csv
# its a module builtin  into python helps with dates and time in this project
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt
import re


class CSV:
    CSV_FILE = "finance_data.csv"  # this is a class variable assoiated with the class
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
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

    @classmethod  # adding the entry
    def add_entry(cls, date, amount, category, description):
        # use pandas/CSV Writer to write in to the file
        # to write the new entry we have to create the new entry in the file
        date = normalize_date(date)
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }  # store in python dictionary
        with open(cls.CSV_FILE, "a", newline="") as csvfile:  # automatically close the file
            # a is pending to the end of the file. were just opening it and then putting cursor at the very end of the file.
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(new_entry)
        print("Entry added succesfully")

    @classmethod  # helps with all transactions on a same date
    def get_transactions(cls, start_date, end_date):
        # convert all dates inside date column to datetime object
        df = pd.read_csv(cls.CSV_FILE)
        # give the access to all the values in the row
        # For the file data
        df["date"] = df["date"].apply(normalize_date)
        df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        # creating a mask is something that we can applt to the different rows inside of a dataframe see we should select the row or not
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # apply to every single row inside of dataframe and its going to filter the different elements
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions found in the given data range.')
        else:
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={
                  "date": lambda x: x.strftime(CSV.FORMAT)}))
            total_income = filtered_df[filtered_df["category"]
                                       == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"]
                                        == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df


def normalize_date(date_str: str) -> str:
    """
    Normalize a date string into dd-mm-YYYY format.
    Accepts separators like / , . space or - and different orders.
    """
    s = str(date_str).strip()

    # Replace commas, dots, slashes, multiple spaces with "-"
    s = re.sub(r'[,./\s]+', '-', s)

    # Try some common formats
    formats = ["%d-%m-%Y", "%d-%m-%y", "%Y-%m-%d", "%m-%d-%Y"]
    for fmt in formats:
        try:
            dt = datetime.strptime(s, fmt)
            return dt.strftime("%d-%m-%Y")  # <- consistent format
        except ValueError:
            continue

    # Fallback: let pandas try
    dt = pd.to_datetime(s, dayfirst=True, errors="coerce")
    if pd.isna(dt):
        raise ValueError(f"Unrecognized date format: {date_str}")
    return dt.strftime("%d-%m-%Y")

# we have to write a function that can call the data in the inorder we want


def add():
    CSV.intialized_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter the today's date: ", allow_default=True, )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):  # creating a graph
    df.set_index('date', inplace=True)
    # we need to set two dataframes income and exxpense
    income_df = df[df["category"] == "Income"].resample(
        "D").sum().reindex(df.index, fill_value=0)  # daily frequency
    expense_df = df[df["category"] == "Expense"].resample(
        "D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index,
             expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3):")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy):")
            end_date = get_date("Enter the end date (dd-mm-yyyy):")
            df = CSV.get_transactions(start_date, end_date)
            if input("Do you want to see a plot?(y/n)").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting:")
            break
        else:
            print("Invalid choice. Enter 1,2 or 3.")


if __name__ == "__main__":
    main()
