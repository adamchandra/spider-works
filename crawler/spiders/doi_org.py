# -*- coding: utf-8 -*-
import scrapy


# class DoiOrgSpider(scrapy.Spider):
#     name = 'doi_org'
#     allowed_domains = ['doi.org']
#     # start_urls = ['http://doi.org/']
#
#     def parse(self, response):
#         pass


# General scraper
class WatrSpider(scrapy.Spider):
    name = 'watrspidr'

    def __init__(self, urlfile=None, *args, **kwargs):
        super(WatrSpider, self).__init__(*args, **kwargs)
        self.start_urls = read_csv(urlfile)

    def parse(self, response):
        pass



import csv
def read_csv(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        lines = [row[3] for row in spamreader]

    return lines
