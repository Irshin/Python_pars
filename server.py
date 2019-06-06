import memcache
from aiohttp import web

from main import get_data

routes = web.RouteTableDef()
memcache_client = memcache.Client(['127.0.0.1:11211'], debug=0)

@routes.get('/')
async def hello(request):
    coins_data = memcache_client.get('coins_data')
    if not coins_data:
        coins_data = await get_data()
        memcache_client.set("coins_data", coins_data, 10)

    return web.json_response(coins_data, headers={'Access-Control-Allow-Origin': '*'})

app = web.Application()
app.add_routes(routes)
web.run_app(app)
