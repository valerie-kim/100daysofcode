"""
Send Birthday Wish Emails using "smtplib"
"""

#yahoo: dummyemail.valkim
#google: dummy.email.valkim

import smtplib
import datetime as dt
import random

MY_EMAIL = "dummy.email.valkim@gmail.com"
MY_PASSWORD = "Haven1997!"
# EMAIL_TO = "dummyemail.valkim@yahoo.com"
EMAIL_TO = "havenkim@uw.edu"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("/Users/valerie/Documents/100days_of_Python/06-23/Day32/quotes.txt") as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=EMAIL_TO, 
            msg=(f"Subject:Monday Motivation | Today's Quote\n\n{random_quote}")
        )
