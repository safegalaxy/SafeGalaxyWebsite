"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.controllers import Controller
from masonite import env
import datetime
from decimal import *
import requests
import boto3
import logging


class PageController(Controller):
    """Controller For Welcoming The User. """

    # def __init__(self, request: Request):
    #     logging.basicConfig(level=logging.DEBUG)
    #     self.logger = logging.getLogger(__name__)

    def home(self, view: View, request: Request):
        # change

        # you have to setup an ngrok link and have a cloudfront url point
        # your ngrok to be able to dev locally. This is pointed at DEV
        stats_cdn_url = env("AWS_CLOUDFRONT")
        # self.logger.info(stats_cdn_url)

        # try:
        #     response = requests.get(stats_cdn_url, timeout=2)

        #     # self.logger.info('Fresh PRice')
        #     # self.logger.info(response)

        #     stats = response.json()
        #     # self.logger.info(stats)
        #     table_count = self.dynamodb_scan_completed()["ScannedCount"]

        #     last_id = 1
        #     if int(table_count) != 0:
        #         last_id = int(table_count)

        #     stats["last_id"] = last_id

        #     self.dynamodb_delete(int(table_count))

        #     self.dynamodb_put(stats)
        #     cached = False
        # except requests.exceptions.Timeout:
        #     table_count = self.dynamodb_scan_completed()["ScannedCount"]

        #     stats = self.dynamodb_get(table_count)["Item"]
        #     # self.logger.info('Cached PRice')
        #     # self.logger.info(stats)
        #     cached = True

        stats = self.dynamodb_get(1)["Item"]
        # self.logger.info('Cached PRice')
        # self.logger.info(stats)
        cached = True

        # stats = {
        #     "last_id": 1,
        #     "holders": "24,338",
        #     "liquidity_generated": "2,162,872.11",
        #     "market_cap": "17,316,553.36",
        #     "volume_24hr": "465,066.76",
        #     "volume_24hr_change": "0.02",
        #     "volume_24hr_direction": "down",
        #     "tokens_burned": "364,432,902,901,376.02",
        #     "current_price": "0.000000017395281",
        #     "price_24hr_change": "0.19",
        #     "price_24hr_direction": "down",
        #     "timestamp_unix": 1618174481,
        #     "timestamp_utc": "2021-04-11 20:54:41 UTC"
        # }

        stats["price_24hr_change"] = round(float(stats["price_24hr_change"]) * 100, 2)
        stats["volume_24hr_change"] = round(float(stats["volume_24hr_change"]) * 100, 2)

        return view.render("pages/home", {
            "cache_buster": datetime.datetime.now().strftime("%s"),
            "path": request.path,
            "year": datetime.date.today().year,
            "stats": stats,
            "cached": cached
        })

    def team(self, view: View, request: Request):
        # team profiles could be pulled dynamically with a DB
        # {"img_url": "/storage/static/images/SafeGalaxy-Mercia.png", "profile_name": "Mircea", "profile_position": "Lead FE Developer", "linkedin_url": "https://www.linkedin.com/in/mircea-sima-b9b855101"},
        # {"img_url": "/storage/static/images/SafeGalaxy-Fenton.png", "profile_name": "Fenton", "profile_position": "Lead DevOps & <br>Platform Engineer", "linkedin_url": "https://www.linkedin.com/in/fenton-haslam-8764b69b"},

        top_profiles_data = [
            {"img_url": "/storage/static/images/Team-card-blank-spencer-SG.png", "profile_name": "Spencer", "profile_position": "CEO & Developer", "linkedin_url": "https://www.linkedin.com/in/spencer-macey/"},
            {"img_url": "/storage/static/images/Team-card-blank-jacob-SG.png", "profile_name": "Jacob", "profile_position": "COO & Developer", "linkedin_url": "https://www.linkedin.com/in/jmcfeldman/"},
            {"img_url": "/storage/static/images/Team-card-blank-jason-SG.png", "profile_name": "Jason", "profile_position": "CTO & Developer", "linkedin_url": "https://www.linkedin.com/in/shunzhou-tan/"},
        ]

        center_profiles_data = [
            {"img_url": "/storage/static/images/Team-card-blank-tim-SG.png", "profile_name": "Tim", "profile_position": "Head of Design", "linkedin_url": "https://www.linkedin.com/in/tim-de-winter-04907184/"},
            {"img_url": "/storage/static/images/Team-card-blank-rijk-SG.png", "profile_name": "Rijk", "profile_position": "Social Media Manager", "linkedin_url": "http://linkedin.com/in/rijk-poelmans-508b87210"},
            {"img_url": "/storage/static/images/Team-card-blank-ben-SG.png", "profile_name": "Ben", "profile_position": "Strategic Partnerships", "linkedin_url": "https://www.linkedin.com/company/safegalaxy-net"},
        ]

        bottom_profiles_data = [
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
            {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "We're Hiring", "job_desc": "We are looking for many talented individuals to help SafeGalaxy reach the stars and beyond. Follow the button below for open positions.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Marketing/Social Media Manager", "job_desc": "Our ideal person has proven experience identifying and engaging influencers, managing influencer outreach programs, and creating engaging, brand worthy content for all our social media platforms.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-3.png", "job_title": "Marketing/Social Media Intern", "job_desc": "Our ideal person has proven experience identifying and engaging influencers, managing influencer outreach programs, and creating engaging, brand worthy content for all our social media platforms.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "HR/Payroll Specialist", "job_desc": "You demonstrate analytical and problem-solving skills with superb communication capability. This individual will need experience in payroll processing, benefits, and possess thorough knowledge of employment related laws and regulations", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-3.png", "job_title": "Executive Assistant", "job_desc": "We are looking for someone who can assist the executive team with meeting scheduling, organization, official correspondence, and other tasks as they are requested. You should be able to demonstrate an ability to work fast and efficiently in fast-paced, high-stress environments.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-1.png", "job_title": "Community Manager", "job_desc": "We are looking for someone who is detail oriented, organized and can demonstrate the ability to work quickly, accurately and under pressure. Must be tech savvy. You should have a positive attitude and the desire to contribute to our team, be self-motivated, and able to work in a fast-paced, high-stress environments", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Community Intern", "job_desc": "We are looking for someone who is detail oriented, organized and can demonstrate the ability to work quickly, accurately and under pressure. Must be tech savvy. You should have a positive attitude and the desire to contribute to our team, be self-motivated, and able to work in a fast-paced, high-stress environments", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
        #     {"img_url": "/storage/static/images/Job-planet-2.png", "job_title": "Technical Project Manager", "job_desc": "We want someone who can be considered to be both a tech guru and an inspiring leader. As someone who is instrumental in the planning and management of both Software Developers and their projects.", "google_form_url": "https://safegalaxy.aidaform.com/Apply"},
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

    def dynamodb_put(self, data):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.put_item(
            Item=data
        )
        return response

    def dynamodb_get(self, last_id):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.get_item(
            Key={
                "last_id": last_id,
            },
        )
        return response

    def dynamodb_delete(self, last_id):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.delete_item(
            Key={
                "last_id": last_id,
            },
        )
        return response

    def dynamodb_scan_completed(self):
        dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=env("AWS_CLIENT"),
            aws_secret_access_key=env("AWS_SECRET"),
            region_name="us-east-1",
            endpoint_url="https://dynamodb.us-east-1.amazonaws.com"
        )
        table = dynamodb.Table("last_price")
        response = table.scan(
            Select="COUNT",
        )
        return response
