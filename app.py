from flask import Flask


class MyApplication:
    """A simple class to represent a Flask application."""

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.add_url_rule("/", "home", self.home_page)

    def home_page(self) -> str:
        """function of the principal route. return a string with a message for a activate user."""

        return "Hello world!"

    def run(self) -> None:
        """Run the application."""

        self.app.run(debug=True, port=5152)


if __name__ == "__main__":

    app = MyApplication()
    app.run()
