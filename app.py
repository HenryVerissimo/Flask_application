from flask import Flask
from src.controllers.routes.login_route import CreateUserRoute


class MyApplication:
    """A simple class to represent a Flask application."""

    def __init__(self) -> None:
        self.app = Flask(__name__, template_folder="src/views/templates")
        self.app.add_url_rule(
            "/create_user", view_func=CreateUserRoute.as_view("create_user")
        )

    def run(self) -> None:
        """Run the application."""

        self.app.run(debug=True, port=5152)


if __name__ == "__main__":

    app = MyApplication()
    app.run()
