"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
import datetime


class PageController(Controller):
    """Controller For Welcoming The User. """

    def home(self, view: View, request: Request):
        # change

        return view.render("pages/home", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path
        })

    def team(self, view: View, request: Request):
        # team profiles could be pulled dynamically with a DB.

        top_profiles_data = [
            {"img_url": "/storage/static/images/SafeGalaxy-Spencer.png", "profile_name": "Spencer", "profile_position": "CEO & Developer", "linkedin_url": "https://www.linkedin.com/in/spencer-macey/"},
            {"img_url": "/storage/static/images/SafeGalaxy-Jacob.png", "profile_name": "Jacob", "profile_position": "COO & Developer", "linkedin_url": "https://www.linkedin.com/in/jmcfeldman/"},
            {"img_url": "/storage/static/images/SafeGalaxy-Jason.png", "profile_name": "Jason", "profile_position": "CTO & Developer", "linkedin_url": "https://www.linkedin.com/in/shunzhou-tan/"},
        ]

        center_profiles_data = [
            {"img_url": "/storage/static/images/SafeGalaxy-Fenton.png", "profile_name": "Fenton", "profile_position": "Lead DevOps & <br>Platform Engineer", "linkedin_url": "https://www.linkedin.com/in/fenton-haslam-8764b69b"},
            {"img_url": "/storage/static/images/SafeGalaxy-Tim.png", "profile_name": "Tim", "profile_position": "Head of Design & <br>Content Creator", "linkedin_url": "https://www.linkedin.com/in/tim-de-winter-04907184/"},
            {"img_url": "/storage/static/images/SafeGalaxy-Mercia.png", "profile_name": "Mircea", "profile_position": "Lead FE Developer", "linkedin_url": "https://www.linkedin.com/in/mircea-sima-b9b855101"},
        ]

        bottom_profiles_data = [
            {"img_url": "/storage/static/images/SafeGalaxy-Ben.png", "profile_name": "Ben", "profile_position": "Strategic Partnerships", "linkedin_url": "https://www.linkedin.com/company/safegalaxy-net"},
            {"img_url": "/storage/static/images/Safe-Galaxy-Socialteam.png", "profile_name": "Social Team", "profile_position": "Ads & Marketing", "linkedin_url": "https://www.linkedin.com/company/safegalaxy-net"},
        ]

        return view.render("pages/team", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "top_profiles_data": top_profiles_data,
            "center_profiles_data": center_profiles_data,
            "bottom_profiles_data": bottom_profiles_data,
        })

    def whitepaper(self, view: View, request: Request):
        # changes

        return view.render("pages/whitepaper", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path
        })

    def how_to_buy(self, view: View, request: Request):
        # changes

        return view.render("pages/how_to_buy", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path
        })

    def jobs(self, view: View, request: Request):
        # changes

        return view.render("pages/jobs", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path
        })
