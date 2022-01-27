from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

'''cart_value = request.args.get('cart_value')
delivery_distance = request.args.get('delivery_distance')
number_of_items = request.args.get('number_of_items')
time = request.args.get('time')'''


# /<int:delivery_distance>/<int:number_of_items>/<string:time>
# , delivery_distance: int, number_of_items: int, time: str

@app.route('/with_parameters')
def with_parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")


# api.add_resource(with_url_variables, "/with_url_variables/<int:cart_value>/<int:delivery_distance>/<int:number_of_items>/<string:time>")

if __name__ == '__main__':
    app.run()
