class fees:
    def __init__(self, cart_value, delivery_distance, number_of_items, time_for_order):
        # setting the instance variables
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time_for_order = time_for_order

    # create a separate functions to calculate the fees for each condition

    def fees_for_distance(self):
        import math
        minimum_fee = 100

        # distance check
        if self.delivery_distance in range(1, 501):
            return minimum_fee
        elif self.delivery_distance in range(501, self.delivery_distance + 1):
            return (math.ceil(self.delivery_distance / 500)) * 100
        else:
            return 0

    def fees_for_number_of_items(self):
        # number of items check
        surcharge = self.number_of_items - 4
        if 1 <= self.number_of_items <= 4:
            return 0
        else:
            # surcharge for additional items above 4 is calculated here
            return surcharge * 50

    def fees_for_friday_rush_hours(self):
        from datetime import datetime
        from flask import abort
        import dateutil.parser as dp

        # time format check
        time_format = "%Y-%m-%dT%H:%M:%SZ"
        try:
            datetime.strptime(self.time_for_order, time_format)
        except ValueError:
            return abort(400, "Wrong time format")

        # ISO string  => convert to unix
        unix_timestamp = dp.parse(self.time_for_order)
        # get the date
        date = unix_timestamp
        # get the hour number
        hours = unix_timestamp.hour
        # get the minutes number
        minutes = unix_timestamp.minute
        # get the second number
        seconds = unix_timestamp.second
        # get the weekday number
        day = date.today().weekday()

        # friday rush hours check
        if day == 4 and 15 <= hours <= 18:
            return 1.1
        elif day == 4 and hours == 19 and minutes == 00 and seconds == 00:
            return 1.1
        else:
            return 1

    def delivery_fees(self):
        distance_delivery_fees = self.fees_for_distance()
        items_delivery_fees = self.fees_for_number_of_items()
        hours_delivery_fees = self.fees_for_friday_rush_hours()  # 1.1 or 1

        # I did not wrap it into int because it should be float
        # surcharge of the carte value
        surcharge = 1000 - self.cart_value
        # surcharge fees will be added on items delivery fees if items number > 4
        final_fees = (distance_delivery_fees + items_delivery_fees) * hours_delivery_fees

        # 10000 cents are 100 Euros
        if self.cart_value >= 10000:
            return 0
        # check if the cart value is less than 1000 cents
        elif self.cart_value < 1000:
            # I could round up the result using round() function to be able to get an integer value,
            # but in some calculation will affect the result.
            return final_fees + surcharge

        # check if the cart value is bigger than 1000 cents
        elif self.cart_value >= 1000:
            # I could round up the result using round() function to be able to get an integer value,
            # but in some calculation will affect the result.
            return final_fees
