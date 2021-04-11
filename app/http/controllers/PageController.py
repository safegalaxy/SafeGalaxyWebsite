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
            "path": request.path,
            "year": datetime.date.today().year
        })

    def team(self, view: View, request: Request):
        # team profiles could be pulled dynamically with a DB

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
            "year": datetime.date.today().year
        })

    def whitepaper(self, view: View, request: Request):
        # changes

        return view.render("pages/whitepaper", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year
        })

    def how_to_buy(self, view: View, request: Request):
        # changes

        return view.render("pages/how_to_buy", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year
        })

    def jobs(self, view: View, request: Request):
        # change

        job_data = [
            {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "Senior Developer", "job_desc": "Mauris at placerat augue. Fusce ornare semper dapibus. Nulla malesuada libero est, ac congue magna consequat elementum. Etiam massa metus, fringilla vel tortor id, rutrum dictum diam. Nulla semper est id ex mollis, quis accumsan arcu varius. ", "google_form_url": ""},
            {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Junior Developer", "job_desc": "Suspendisse varius felis ac nisi scelerisque, ac gravida ipsum feugiat. Nullam ut arcu at ligula pellentesque rutrum eget ut nunc. Etiam dictum odio iaculis placerat maximus. ", "google_form_url": ""},
            {"img_url": "/storage/static/images/Job-planet-3.png", "job_title": "Senior Blockchain Developer", "job_desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sollicitudin massa a pretium laoreet. Praesent tortor tellus, lobortis vel lectus sit amet, mollis blandit sapien. ", "google_form_url": ""},

            {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "Senior Developer", "job_desc": "Mauris at placerat augue. Fusce ornare semper dapibus. Nulla malesuada libero est, ac congue magna consequat elementum. Etiam massa metus, fringilla vel tortor id, rutrum dictum diam. Nulla semper est id ex mollis, quis accumsan arcu varius. ", "google_form_url": ""},
            {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Junior Developer", "job_desc": "Suspendisse varius felis ac nisi scelerisque, ac gravida ipsum feugiat. Nullam ut arcu at ligula pellentesque rutrum eget ut nunc. Etiam dictum odio iaculis placerat maximus. ", "google_form_url": ""},
        ]

        return view.render("pages/jobs", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "job_data": job_data,
            "year": datetime.date.today().year
        })

    def tos(self, view: View, request: Request):
        # changes

        return view.render("pages/tos", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year
        })

    def policy(self, view: View, request: Request):
        # changes

        return view.render("pages/policy", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year
        })
