"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
import datetime


class HomeController(Controller):
    """Controller For Welcoming The User."""

    def home(self, view: View, request: Request):
        # changes2222222222

        return view.render("pages/home", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
        })

    def team(self, view: View, request: Request):
        # changes

        return view.render("pages/team", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
        })

    def whitepaper(self, view: View, request: Request):
        # changes

        return view.render("pages/whitepaper", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
        })

    def how_to_buy(self, view: View, request: Request):
        # changes

        return view.render("pages/how_to_buy", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
        })
