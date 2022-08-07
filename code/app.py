from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

# Every resource is a class
class Student(Resource):  # Inherits from Resource
    def get(self, name):
        return {"student": name}

api.add_resource(Student, "/student/<string:name>")

app.run(port=5000)

