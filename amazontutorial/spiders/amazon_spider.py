# -*- coding: utf-8 -*-
import scrapy, time
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/Books/b?ie=UTF8&node=549028"
        ]


    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.acs-product-block__product-title .a-truncate-cut::text').extract()   
        product_author = response.css('.acs-product-block__contributor .a-truncate-cut').css('::text').extract()   
        product_price = response.css('.acs-product-block__price--buying span::text').css('::text').extract()   
        product_imagelink = response.css('#twoPassCarousel img:attr(src)').extract() 

        items['product_name'] = product_name 
        items['product_author'] = product_author
        items['product_price'] = product_price 
        items['product_imagelink'] = product_imagelink 

        time.sleep(5)
        
        yield items
