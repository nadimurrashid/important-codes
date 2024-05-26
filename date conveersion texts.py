dates = ["2023-11-06", "2023-11-13" ,"2023-11-20" ,"2023-11-27"]
from datetime import datetime


def date_conversion(date_string):

    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    day_of_week = date_object.strftime("%A")
    month = date_object.strftime("%B")
    day_of_month = date_object.day
    year = date_object.year

    return f"Week commencing {day_of_week[0:3]} {day_of_month} {month[0:3]} {year}"

detailed_texts = []

for Sday in dates:
    detailed_texts.append(date_conversion(Sday))

print(detailed_texts)