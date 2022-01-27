from fees import fees
from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api

app = Flask("Delivery Fees")
api = Api(app)


class Adder(Resource):
    def get(self):
        args = request.args
        print(args)  # For debugging

        #params eval
        cart_value = args['cart_value']
        delivery_distance = args['delivery_distance']
        number_of_items = args['number_of_items']
        time_for_order = args['time']
        print(type(cart_value))
        print(type(delivery_distance))
        print(type(number_of_items))
        print(type(time_for_order))

        if len(delivery_distance) == 0 or len(cart_value) == 0 or len(number_of_items) == 0 or len(time_for_order) == 0:
            print(args.get("delivery_distance"))
            return jsonify("Invalid Parameter"), abort(400)

        else:

            cart_value = float(args['cart_value'])
            delivery_distance = int(args['delivery_distance'])
            number_of_items = int(args['number_of_items'])
            time_for_order = str(args['time'])

            # if args.get("delivery_distance") is None or args.get("cart_value") is None or args.get(
            #         "number_of_items") is None or args.get("time_for_order") is None:
            #     return jsonify("Invalid Parameter"), abort(400)

            print("cart value is", cart_value)
            print("delivery distance is", delivery_distance)
            print("number of items are", number_of_items)
            print("time is", time_for_order)

            # we are calling here class fees
            db_utils = fees(cart_value, delivery_distance, number_of_items, time_for_order)
            # we are calling the fees method to calculate the delivery_fees
            cursor = db_utils.delivery_fees(cart_value, delivery_distance, number_of_items,
                                            time_for_order)  # without surchage
            print(cursor)
            # get day surcharge either 1 or 1.1

            if cursor > 1500:
                return jsonify(f"delivery_fee: {1500}")
            elif delivery_distance <= 0 or cart_value <= 0 or number_of_items <= 0 or len(time_for_order) == 0:
                print(args.get("delivery_distance"))
                return jsonify("Invalid Parameter"), abort(400)
            else:
                return jsonify(f"delivery_fee: {cursor}")


api.add_resource(Adder, '/fees')

if __name__ == '__main__':
    app.run()
