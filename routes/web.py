"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'HomeController@home'),
    Get('/team', 'HomeController@team'),
    Get('/whitepaper', 'HomeController@whitepaper'),
    Get('/how-to-buy', 'HomeController@how_to_buy'),

    # API route
    Get('/public/stats', 'StatsController@stats'),
]
