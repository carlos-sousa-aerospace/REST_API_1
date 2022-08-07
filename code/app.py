from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []


# Every resource is a class
class Item(Resource):  # Inherits from Resource
    def get(self, name):
        try:
            return next(item for item in items if item["name"] == name)
        except StopIteration:
            return {"Error 507": "Item not found in the collection"}, 404

    def post(self, name):
        for item in items:
            if item["name"] == name:
                return {"Error 509": f"The item {name} is already in the collection. No actions will be taken"}, 400

        data = request.get_json()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    def delete(self, name):
        try:
            item = next(item for item in items if item["name"] == name)
            items.remove(item)
            return item
        except StopIteration:
            return {"Error 507": "Item not found in the collection"}, 404

    def put(self, name):
        try:
            item = next(item for item in items if item["name"] == name)
            data = request.get_json()

            item["price"] = data["price"]
            return item, 200
        except StopIteration:
            return {"Error 507": "Item not found in the collection"}, 404


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
