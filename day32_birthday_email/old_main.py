''' Send an automated email to people on a list on their birthday '''
import smtplib
import datetime as dt
import random


with open("day32/quotes.txt", "r") as f:
    quotes = f.read().splitlines()


now = dt.datetime.now()
RANDOM_QUOTE = random.choice(quotes)
if now.weekday() == 5:
    password= "mbklkgkojiujsfkz"
    my_email = "des.barrett.sub@gmail.com"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="des.barrett@gmail.com",
            msg=f"Subject: You Quote for Tuesday\n\n{RANDOM_QUOTE}")
