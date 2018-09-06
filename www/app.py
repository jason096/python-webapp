import logging
import json
import time
import asyncio
import os
from datetime import datetime
from aiohttp import webbrowser

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.response(body=b'<h1>Awesome</h1>')


def init(loop):
    app = web.application(loop=loop)
    app.router.add_route("GET","/",index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()