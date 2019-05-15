from aiohttp import web

from main import get_data

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    data = await get_data()
    return web.json_response(data, headers={'Access-Control-Allow-Origin': '*'})

app = web.Application()
app.add_routes(routes)
web.run_app(app)
