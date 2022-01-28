from fees import fees
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
from datetime import datetime as dt

app = Flask("Delivery Fees")
api = Api(app)


class Adder(Resource):
    def get(self):
        args = request.args
        print(args)  # For debugging

        # params eval
        cart_value = args['cart_value']
        delivery_distance = args['delivery_distance']
        number_of_items = args['number_of_items']
        time_for_order = args['time']

        if len(delivery_distance) == 0 or len(cart_value) == 0 or len(number_of_items) == 0 or len(time_for_order) == 0:
            return abort(400, "one or more parameter's value is/are empty")
        else:
            try:
                cart_value = float(args['cart_value'])
            except ValueError:
                return abort(400, "String value is passed in one of the parameters")
            try:
                delivery_distance = int(args['delivery_distance'])
                number_of_items = int(args['number_of_items'])
            except ValueError:
                return abort(400, "String value is passed in one of the parameters or a float number")

            # check time format is done in fees.py file
            time_for_order = str(args['time'])
            time_format = "%Y-%m-%dT%H:%M:%SZ"
            try:
                dt.strptime(time_for_order, time_format)
            except ValueError:
                return abort(400, "Wrong time format")

            # we are calling here class fees
            db_utils = fees(cart_value, delivery_distance, number_of_items, time_for_order)
            # we are calling the delivery_fees() method to calculate the delivery fees
            final_delivery_fees = db_utils.delivery_fees()

            # check if the delivery fees are more than 1500
            if final_delivery_fees > 1500:
                return jsonify(f"delivery_fee: {1500}")
            elif delivery_distance <= 0 or cart_value <= 0 or number_of_items <= 0:
                return abort(400, "parameter's values are invalid, negative or 0")
            else:
                return jsonify(f"delivery_fee: {final_delivery_fees}")


api.add_resource(Adder, '/fees')

if __name__ == '__main__':
    app.run()
