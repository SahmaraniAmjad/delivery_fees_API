from fees import fees
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api

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

        if delivery_distance is None or cart_value is None or number_of_items is None or time_for_order is None:
            return jsonify("Invalid Parameter"), abort(400)
        else:
            cart_value = float(args['cart_value'])
            delivery_distance = int(args['delivery_distance'])
            number_of_items = int(args['number_of_items'])
            time_for_order = str(args['time'])

        print("cart value is", cart_value)
        print("delivery distance is", delivery_distance)
        print("number of items are", number_of_items)
        print("time is", time_for_order)

        # we are calling here class fees
        db_utils = fees(cart_value, delivery_distance, number_of_items, time_for_order)
        # we are calling the fees method to calculate the delivery_fees
        cursor = db_utils.delivery_fees(cart_value, delivery_distance, number_of_items, time_for_order) # without surchage
        # get day surcharge either 1 or 1.1

        return jsonify("delivery_fees: " + str(cursor))

        '''cart_value = args.get("cart_value")
        delivery_distance = args.get("delivery_distance")
        number_of_items = args.get("number_of_items")
        time = args.get("time")

        if delivery_distance is None or cart_value is None or number_of_items is None or time is None:
            return jsonify("Invalid Parameter"), abort(400)
        else: #cursor == 40
            #cursor >= 15 cursor = 15 '''




api.add_resource(Adder, '/fees')


if __name__ == '__main__':
    app.run()
