"""Web Routes."""

from masonite.routes import Get, Post

ROUTES = [
    Get('/', 'PageController@home'),
    Get('/team', 'PageController@team'),
    Get('/whitepaper', 'PageController@whitepaper'),
    Get('/how-to-buy', 'PageController@how_to_buy'),
    Get('/jobs', 'PageController@jobs'),

    # API route
    Get('/public/stats', 'StatsController@stats'),
]
