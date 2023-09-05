''' Send a random happy birthday email if a birthday matches todays date '''
import datetime as dt
import random
import smtplib
import pandas as pd

def send_mail(host, user_email, password, send_to, message):
    '''  send email given host, user, password, email recipient, and message '''
    with smtplib.SMTP(host) as connection:        
        connection.starttls() # transport layer security
        connection.login(user=user_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=message)

# Read the data from csv
df = pd.read_csv("day32/birthdays.csv")
birthday_records = df.to_dict(orient="records")

# get todays date
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# email details
password= ""
my_email = ""
host = "smtp.gmail.com"
send_to = ""
message = f"Subject: Happy Birthday\n\n"

# loop through birthday list, check if today date matches one on
# list and send personalised email 
for birthday in birthday_records:
    if birthday['month'] == month and birthday['day'] == day:
        random_num = random.choice(range(1,4))
        random_letter = f"letter_{str(random_num)}"
        with open(f"day32/letter_templates/{random_letter}.txt") as letter:
            lines = letter.readlines()
            formated_lines = ''.join(
                [line.replace('[NAME]', f"{birthday['name']}") for line in lines])
            message = message+formated_lines
            send_mail(host, my_email, password, send_to, message)
