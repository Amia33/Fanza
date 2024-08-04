# pylint: disable=locally-disabled, arguments-differ
"""Initialize label ids to fetch, to save time usage"""

import re
import scrapy


class InitSpider(scrapy.Spider):
    """Spider: Initialize"""
    name = "Initialize"

    def start_requests(self):
        cook = {
            "age_check_done": "1"
        }
        for label in range(1, 3000000):
            dest_a = "https://www.dmm.co.jp/digital/videoa/-/list/?label=" + \
                str(label) + "&sort=date&limit=120"
            dest_c = "https://www.dmm.co.jp/digital/videoc/-/list/?label=" + \
                str(label) + "&sort=date&limit=120"
            yield scrapy.Request(dest_a, cookies=cook, callback=self.parse)
            yield scrapy.Request(dest_c, cookies=cook, callback=self.parse)

    def parse(self, response):
        if "videoa" in response.url:
            with open("videoa.txt", "a", encoding="utf-8") as f:
                f.write(re.findall(r'label=([0-9]*)', response.url)[0] + "\n")
        if "videoc" in response.url:
            with open("videoc.txt", "a", encoding="utf-8") as f:
                f.write(re.findall(r'label=([0-9]*)', response.url)[0] + "\n")
