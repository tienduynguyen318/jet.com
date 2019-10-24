# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from typing import List

import scrapy




class JetcomItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Review(object):
    star: int
    title: str
    description: str
    created_at: str

    def to_json(self):
        return {
            "star": self.star,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
        }


class ListReviews(object):
    item: List[Review]

    def to_json(self):
        return [i.to_json() for i in self.item]


class Product(object):
    pid: str
    name: str
    description: str
    category: str
    vendor: str
    price: str
    img_url: str
    product_url: str
    avg_star: str
    total_reviews: int
    number_of_reviewed_users: int
    reviews: ListReviews

    def to_json(self):
        return {
            "page_id": self.pid,
            "name": self.name,
            "description": self.description,
            "vendor": self.vendor,
            "category": self.category,
            "price": self.price,
            "img_url": self.img_url,
            "product_url": self.product_url,
            "avg_star": self.avg_star,
            "total_review": self.total_reviews,
            # "number_of_reviewed_users": self.number_of_reviewed_users,
            # "reviews": self.reviews.to_json(),
        }
