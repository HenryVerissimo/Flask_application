from flask import render_template, request
from flask.views import MethodView
from flask import Blueprint


class LoginBlueprint:
    """This calss is a Blueprint to register all login routes"""

    def __init__(self):
        self.login_bp = Blueprint("login", __name__, url_prefix="/login")
        self.build_routes()

    def build_routes(self):
        self.login_bp.add_url_rule(
            "/create_user", view_func=CreateUserRoute.as_view("create_user")
        )


class CreateUserRoute(MethodView):
    """This class is a route with a form to create a new user on the web application"""

    methods = ["GET", "POST"]

    def get(self):
        return render_template(r"create_user.html")

    def post(self):
        pass


class LoginUserRoute(MethodView):
    """This class is a route with a form to login on the web application"""

    def get(self):
        pass

    def post(self):
        pass


class ResetPasswordRoute(MethodView):
    """This class is a route with a form to reset account password on the web application"""

    def get(self):
        pass

    def post(self):
        pass
