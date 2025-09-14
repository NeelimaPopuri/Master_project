# using this data entry file to write all the functions related to getting information from the user
from datetime import datetime

date_format = "%d,%m,%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

# recurrsive function


def get_date(prompt, allow_default=False):
    # prompt is going to ask the user to input before they give us the date
    # Use the default will be giving the value by default when we press enter it will select the current date
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime("%d,%m,%Y")
    except ValueError:
        print("Invalid date fromat. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input(
        "Enter the category('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()


def get_description():
    pass
