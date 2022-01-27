from datetime import datetime, date
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import schedule
import time


import dateutil.parser as parser


class fees:
    def __init__(self, cart_value, delivery_distance, number_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time

    '''def all_fridays(year):

        from datetime import datetime, timedelta, date
        time = datetime(year, 1, 1, 15, 0, 0, 0)  # January 1st
        end_time = datetime(year, 1, 1, 19, 0, 0, 0)  # January 1st
        time += timedelta(days=11 - time.weekday())  # First Friday
        while time.year == year:
            yield time
            time += timedelta(days=7)

    for time in all_fridays(year=2022):
        print(time.isoformat())'''

    #time = "Y-m-d\TH\Z"
    time1 = datetime.now().isoformat(timespec="hours") + "Z"
    #print(parser.isoparse('2022-01-28T15:00:00Z'))
    time2 = datetime.fromisoformat('2022-12-12')
    #time = 'Fri, 24 Jan 2022 15:00:00Z'
    date = datetime.strptime('Fri, 24 Jan 2022 15:00:00', '%a, %d %b %Y %H:%M:%S')

    #print(date.isoformat())
    #print(time1)
    #print(time2)


    #import sys
    #print(sys.getrecursionlimit())



    #NumberOfSamples = 10
    rush_hours = pd.offsets.CustomBusinessHour(start="15:00", end="20:00", weekmask="Fri")
    dates = pd.date_range(start='20220101', end='20221231', freq=rush_hours)
    df3 = DataFrame(index=dates)
    df3.index = df3.index.map(lambda x: datetime.strftime(x, '%Y-%m-%dT%H:%M:%SZ'))

    #df3.to_csv('dates.txt', header=False)

    for index, row in df3.iterrows():
        print(f"{index}")

    #print(df3)
    #print(date.now().isoformat())

    '''def job():
        print("I'm working...")

    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)'''
