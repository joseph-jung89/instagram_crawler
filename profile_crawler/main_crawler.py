import re
import json

from scrapy import Spider
from scrapy.http import Request


class InstagramProfilePageScraper(Spider):
	main_url = 'https://www.instagram.com'

	def start_requests(self):
		yield Request(
			url=self.main_url,
			callback=self.handle_main_page_response
		)

	def handle_main_page_response(self, response):
		import pdb; pdb.set_trace()

