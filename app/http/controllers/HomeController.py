"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
import datetime


class HomeController(Controller):
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request):
        # changes

        return view.render("pages/home", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
        })
