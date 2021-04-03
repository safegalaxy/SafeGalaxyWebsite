"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'HomeController@show'),
]
