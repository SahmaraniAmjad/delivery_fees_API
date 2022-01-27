# we are importing the modules we are going to use
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort

# When you make a new flask app
app = Flask(__name__)
api = Api(app)

'''DeliveryFees = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}'''

# RequestParser will validate the multiple arguments in a single request
cart_put_args = reqparse.RequestParser()
cart_put_args.add_argument("cart_value", type=int, help="you forget the amount of the shopping", required=True)
cart_put_args.add_argument("delivery_distance", type=int,
                           help="you forget the distance between the store and the customer's location in meters",
                           required=True)
cart_put_args.add_argument("number_of_items", type=int,
                           help="you forget the number of items in the customer's shopping cart", required=True)
cart_put_args.add_argument("time", type=str, help="you forget the time of delivery", required=True)


cart_value = request.args.get('cart_value')
delivery_distance = request.args.get('delivery_distance')
number_of_items = request.args.get('number_of_items')
time = request.args.get('time')

Carts = {}

Fees = {}

@app.route('/with_url_variables/<int:cart_value>/<int:delivery_distance>/<int:number_of_items>/<string:time>')
def with_url_variables(cart_value: int, delivery_distance: int, number_of_items: int, time: str):
    fees = cart_value + delivery_distance + number_of_items
    return jsonify(message="fees: " + fees)


def abort_if_cart_id_doesnt_exit(cart_id):
    if cart_id not in Carts:
        abort(404, message="Cloud not find the cart.....")


# we will do our first resource in this Api
# will be able to handle a put, get, and delete requests
'''class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data": "Posted"}'''


class Cart(Resource):
    def get(self, cart_id):
        abort_if_cart_id_doesnt_exit(cart_id)
        return Carts[cart_id]

    # create a video
    def put(self, cart_id):
        args = cart_put_args.parse_args()
        Carts[cart_id] = args
        return Carts[cart_id], 201

    # add this to the resource and make it accessible to a specific url


def DeliveryFees(Resource):
    def get(self, delv_fee):
        args = cart_put_args.parse_args()
        return Fees[delv_fee]


# how to pass parameters
'''api.add_resource(HelloWorld, "/helloworld/<string:name>")'''
api.add_resource(Cart, "/cart/<int:cart_id>")

# it will start our server and our Flask application
if __name__ == "__main__":
    app.run(debug=True)
