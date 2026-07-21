##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib, pandas, random

PLACEHOLDER = "[NAME]"


my_email = "n8434109@gmail.com"
my_password = "Testemail1234!"

app_password = "gkyyoacmurxwodep"



# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
# #print(data[data.day == "Monday"])

today = dt.datetime.now()
day = today.day
month = today.month
year = today.year

letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]



todays_bithday = birthday_data[(birthday_data["month"] == month) & (birthday_data["day"] == day)]

if todays_bithday.empty:
    print("No Birthdays today")
else:
    for _, row in todays_bithday.iterrows():

        name = row["name"]
        email = row["email"]

      # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(letter_list)

        with open(f"./letter_templates/{letter}") as letter_file:
            contents = letter_file.read()
            birthday_message = contents.replace(PLACEHOLDER, name)
            
        


        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=birthday_message)
            









