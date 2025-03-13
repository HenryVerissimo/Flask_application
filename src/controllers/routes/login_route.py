from flask import render_template, request
from flask.views import MethodView


class CreateUserRoute(MethodView):
    methods = ["POST", "GET"]

    def get(self):
        return render_template(r"create_user.html")

    def post(self):
        pass
