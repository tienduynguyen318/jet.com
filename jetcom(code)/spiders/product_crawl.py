# -*- coding: utf-8 -*-
import scrapy

from ..items import Product


# input: crawl sản phầm từ jet.com
# output: dữ liệu được lưu dưới dạng json
# dữ liệu cần có Department, Category, url, tổng số review, số sao trung bình, từng review và
# số sao của từng review, người review có recommend sản phẩm ko(T,F,null),
# tên người review, ngày review

class ProductCrawlSpider(scrapy.Spider):
    name = 'product-crawl'
    allowed_domains = ['jet.com']
    start_urls = ['http://jet.com/']

    def parse(self, response):
        p = Product()

        # Extract category
        parent_levels = response.css("div.jonYRR > div a::text").extract()
        leaf_level = response.css("div.jonYRR > div span::text").extract_first()
        parent_levels.append(leaf_level)
        category = parent_levels

        # Extract price
        price = response.css("div.dsOONV > span::text").extract_first()
        title = response.css("h1.MdBQM span::text").extract_first()
        total_reviews = response.css("div.kCNNMd > div > div")[0].css("div")[4].css(
            "div > div > a::text").extract_first()
        avg_stars = ",".join(
            response.css("div.kCNNMd > div > div")[0].css("div")[4].css("div > div > img::attr(src)").extract())
        product_url = response.url
        vendor = response.css("div.eDtJay > div")[1].css("div > a::text").extract_first()

        p.name = title
        p.price = price
        p.total_reviews = int(total_reviews)
        p.product_url = product_url
        p.avg_star = avg_stars
        p.vendor = vendor

        with open("product_metadata.json", "a+") as f:
            f.write(p.to_json() + "\n")
