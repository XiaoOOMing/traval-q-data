# -*- coding: utf-8 -*-
import scrapy


class QunaerhomeSpider(scrapy.Spider):
    name = 'qunaerhome'
    allowed_domains = ['touch.piao.qunar.com']
    start_urls = ['http://touch.piao.qunar.com/']

    def parse(self, response):
        swiperLists = response.css('.mpw-swipe-wrap .swipe-img::attr(src)').extract()
        swipers = []
        id = 0
        for swiper in swiperLists:
            swipers.append({
                "id": id,
                "imgUrl": swiper
            })
            id = id + 1

        iconLists = response.css('.mp-category-item')
        iconList = []
        id = 0
        for iconListItem in iconLists:
            iconList.append({
                "id": id,
                "title": iconListItem.css('.keywords::text').extract_first(),
                "imgUrl": iconListItem.css('img::attr(src)').extract_first()
            })
            id = id + 1

        hot_sales = response.css('.mp-hotsale-item')
        hot_sale = []
        id = 0
        for hot_item in hot_sales:
            hot_sale.append({
                "id": id,
                "title": hot_item.css('.mp-hotsale-sight::text').extract_first(),
                "price": hot_item.css('.mpg-price-num::text').extract_first(),
                "imgUrl": hot_item.css('.mp-hotsale-imgcon img::attr(src)').extract_first(),
            })
            id = id + 1

        recommends = response.css('.mp-like-item')
        recommendLists = []
        id = 0
        for recommend_item in recommends:
            recommendLists.append({
                "id": id,
                "title": recommend_item.css('.mp-like-title::text').extract_first(),
                "comment": recommend_item.css('.mp-comment-num::text').extract_first(),
                "score": recommend_item.css('.mpf-starlevel::attr(data-score)').extract_first(),
                "price": recommend_item.css('.mpg-price-num::text').extract_first(),
                "address": recommend_item.css('.mp-like-address::text').extract_first(),
                "imgUrl": recommend_item.css('.mp-like-img::attr(src)').extract_first(),
                "info": recommend_item.css('.mp-ellipsis2::text').extract_first() if recommend_item.css('.mp-ellipsis2::text').extract_first() else ''
            })
            id = id + 1

        weekends = response.css('.mp-product-item')
        weekendList = []
        id = 0
        for weekend in weekends:
            weekendList.append({
                "id": id,
                "title": weekend.css('.product-name::text').extract_first(),
                "desc": weekend.css('.product-desc::text').extract_first(),
                "imgUrl": weekend.css('img::attr(src)').extract_first(),
            })
            id = id + 1

        res = {
            "swipers": swipers,
            "iconList": iconList,
            "hot_sale": hot_sale,
            "recommendLists": recommendLists,
            "weekendList": weekendList
        }
        yield res
