#！/usr/bin/env python3
#-*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
	await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

	u = User(name='Cest', email='cest@example.com', passwd='1234567890', image='about:blank')
	print(u)
	await u.save()


loop=asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()