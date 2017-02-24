#!/user/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "lingjichen"

"""
async web application
"""

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html',charset = 'UTF-8')

#异步处理网站请求
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9001)
    logging.info('server started ad http://127...1:900...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()