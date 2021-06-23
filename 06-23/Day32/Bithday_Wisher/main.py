##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "<Enter Your Email>"
MY_PASSWORD = "<Enter Your Password>"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthday_data = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): 
        data_row for (index, data_row) in birthday_data.iterrows()
    }
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=(f"Subject:Happy Birthday!\n\n{contents}")
        )

