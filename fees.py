class fees:
    def __init__(self, cart_value, delivery_distance, number_of_items, time_for_order):
        # we are setting the instance variables
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time_for_order = time_for_order

        '''#%Y%m%dT%H%M%S.%fZ
                  #%Y-%m-%dT%H:%M:%S%Z

                  elif time_for_order.format() != '%Y-%m-%d':
                      return jsonify("Invalid Parameter"), abort(400)'''

    # create a separate functions to calculate the fees for each condition

    def fees_for_distance(self):
        import math
        # print(self.delivery_distance)
        minimum_fee = 100

        # we just need math.ceil
        def round_up(n, decimals=0):
            multiplier = 10 ** decimals
            return math.ceil(n * multiplier) / multiplier

        # if delivery_distance < 0:
        # print("Error, distance can't be negative")
        if self.delivery_distance in range(1, 501):
            return minimum_fee
        elif self.delivery_distance in range(501, self.delivery_distance + 1):
            return (round_up(self.delivery_distance / 500)) * 100
        else:
            return 0

    def fees_for_number_of_items(self, number_of_items):
        self.number_of_items = number_of_items
        if 1 <= number_of_items <= 4:
            return 0
        else:
            return (number_of_items - 4) * 50

    def fees_for_friday_rush_hours(self, time_for_order):
        from datetime import date, datetime
        import dateutil.parser as dp
        # check the hour
        # ISO string  => convert to unix
        print(f"time_for_order_1: {time_for_order}")
        print(f"format of time_for_order: {format(time_for_order)}")
        f = "%Y-%m-%dT%H:%M:%S"
        try:
            datetime.strptime(time_for_order, f)
            unix_timestamp = dp.parse(time_for_order)

            print(f"Unix_timestamp iso format: {unix_timestamp.isoformat()}")

            print(f"Unix_timestamp iso format: {unix_timestamp.isoformat()}")
            print(f"time_for_order format:{time_for_order.format()}")
            hours = unix_timestamp.hour
            minutes = unix_timestamp.minute
            seconds = unix_timestamp.second
            day = date.today().weekday()

            print(f"unix_timestamp: {unix_timestamp}\n day: {day} \n hour: {hours} \n minutes: {minutes} \n seconds: {seconds}")
            if day == 4 and 15 <= hours <= 18 and 00 <= minutes <= 59 and 00 <= seconds <= 59:
                return 1.1
            elif day == 4 and hours == 19 and minutes == 00 and seconds == 00:
                return 1.1
            else:
                return 1
        except ValueError:
            print("I am here")
            return False


    def delivery_fees(self, cart_value, delivery_distance, number_of_items, time_for_order):
        distance_delivery_fees = self.fees_for_distance()
        items_delivery_fees = self.fees_for_number_of_items(number_of_items)
        hours_delivery_fees = self.fees_for_friday_rush_hours(time_for_order)  # 1.1 or 1
        print(f"friday_delivery_fees :{hours_delivery_fees}")

        surcharge = int(1000 - cart_value)
        fees_with_surcharge = distance_delivery_fees + items_delivery_fees + surcharge
        fees_without_surcharge = distance_delivery_fees + items_delivery_fees

        # 10000 cents are 100 Euros
        if cart_value >= 10000:
            return 0

        elif cart_value < 1000:
            print("Case one")
            return int(fees_with_surcharge * hours_delivery_fees)

        elif cart_value >= 1000:
            print("Case tow")
            return int(fees_without_surcharge * hours_delivery_fees)
