"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
import datetime
import requests


class PageController(Controller):
    """Controller For Welcoming The User. """

    def home(self, view: View, request: Request):
        # change

        stats_cdn_url = "https://d13wpvp4xr14sc.cloudfront.net"

        response = requests.get(stats_cdn_url)

        stats = response.json()

        return view.render("pages/home", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year,
            "stats": stats
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
        # changes

        job_data = [
            {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "Blockchain Developer", "job_desc": "We are looking for a full-time DApp/ DeFi Developer with Solidity skills who can work on a distributed (remote) team to continue the development and improvement of our platform, DeFi product suite, and technology strategy.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Marketing/Social Media Manager", "job_desc": "Our ideal person has proven experience identifying and engaging influencers, managing influencer outreach programs, and creating engaging, brand worthy content for all our social media platforms.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-3.png", "job_title": "Marketing/Social Media Intern", "job_desc": "Our ideal person has proven experience identifying and engaging influencers, managing influencer outreach programs, and creating engaging, brand worthy content for all our social media platforms.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "HR/Payroll Specialist", "job_desc": "You demonstrate analytical and problem-solving skills with superb communication capability. This individual will need experience in payroll processing, benefits, and possess thorough knowledge of employment related laws and regulations", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-3.png", "job_title": "Executive Assistant", "job_desc": "We are looking for someone who can assist the executive team with meeting scheduling, organization, official correspondence, and other tasks as they are requested. You should be able to demonstrate an ability to work fast and efficiently in fast-paced, high-stress environments.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "Community Manager", "job_desc": "We are looking for someone who is detail oriented, organized and can demonstrate the ability to work quickly, accurately and under pressure. Must be tech savvy. You should have a positive attitude and the desire to contribute to our team, be self-motivated, and able to work in a fast-paced, high-stress environments", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
            {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Community Intern", "job_desc": "We are looking for someone who is detail oriented, organized and can demonstrate the ability to work quickly, accurately and under pressure. Must be tech savvy. You should have a positive attitude and the desire to contribute to our team, be self-motivated, and able to work in a fast-paced, high-stress environments", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
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
