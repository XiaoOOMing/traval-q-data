# -*- coding: utf-8 -*-
import scrapy


class GowhereSpider(scrapy.Spider):
    name = 'gowhere'
    allowed_domains = ['touch.piao.qunar.com']
    start_urls = ['http://touch.piao.qunar.com/touch/toNewCityList.htm']

    def parse(self, response):
        hot_cities = response.css('#city-domestic .mp-tr3 li a::text').extract()

        alphabets = response.css('#city-domestic h2::text').extract()
        alphabets.pop(0)
        alphabets.pop(0)

        cities_name_nodes = response.css('#city-domestic .mp-list')
        cities_name_nodes.pop(0)
        cities_name = []
        for cities_name_node in cities_name_nodes:
            cities_name.append(cities_name_node.css('li a::text').extract())

        cityList = {}
        key = 0
        for alphabet in alphabets:
            cityList[alphabet] = cities_name[key]
            key += 1

        hotCityList = []
        key = 0
        for hot_city in hot_cities:
            hotCityList.append({
                "id": key,
                "title": hot_city
            })
            key += 1

        alphabetList = []
        key = 0
        for alphabet in alphabets:
            alphabetList.append({
                "id": key,
                "title": alphabet
            })
            key += 1

        cityLists = []
        key = 0
        for keyname in cityList:
            cityLists.append({
                "id": key,
                "alpha": keyname,
                "cities": cityList[keyname]
            })
            key += 1

        res = {
            "hot_cities": hotCityList,
            "city_alphabets": alphabetList,
            "cityList": cityLists
        }
        yield res
