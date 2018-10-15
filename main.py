import configparser
import json
import mailSender
import datetime

config = configparser.ConfigParser()
config.read('config.ini')

# json with dates of exams
with open('calendar.json') as json_data:
    calendar = json.load(json_data)

# list with dates that we are interested in
datesToCheck = []

# next week
datesToCheck.append((datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d"))

for dt, val in calendar.items():
    if dt in datesToCheck:
        mailSender.sendMail(
                config['MAIL_INFO']['FROM'],
                config['MAIL_INFO']['TO'],
                config['MAIL_INFO']['SUBJECT'],
                config['MAIL_INFO']['BODY'].format(dt, val))
