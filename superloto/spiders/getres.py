# -*- coding: utf-8 -*-
import scrapy
import json
from .. import items
from scrapy import Request

class GetresSpider(scrapy.Spider):
    name = 'getres'
    allowed_domains = ['www.millipiyango.gov.tr']
    start_urls = ['http://www.millipiyango.gov.tr/sonuclar/listCekilisleriTarihleri.php?tur=superloto']

    def parse(self, response):
        dates = json.loads(response.css('p::text').extract_first())
        json_urls = ['http://www.millipiyango.gov.tr/sonuclar/cekilisler/superloto/' + elem["tarih"] + '.json' for elem in dates]
        for url in json_urls:
            yield Request(url, self.get_json_data)

    def get_json_data(self, response):
        item = items.SuperlotoItem()
        item["data"] = json.loads(response.css('body p::text').extract_first())
        return item["data"]
