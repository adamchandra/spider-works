# -*- coding: utf-8 -*-
import scrapy


class DoiOrgSpider(scrapy.Spider):
    name = 'doi_org'
    allowed_domains = ['doi.org']
    # start_urls = ['http://doi.org/']

    def parse(self, response):
        pass
