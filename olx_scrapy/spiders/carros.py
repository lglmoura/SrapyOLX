# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    #allowed_domains = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']
    start_urls = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        
    
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
        ).extract_first()
        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
        ).extract_first()
        yield {
            'title': title,
            'year': year,
            'ports': ports,
        }
       

