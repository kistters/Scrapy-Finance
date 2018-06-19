# -*- coding: utf-8 -*-
import scrapy


class TesouroDiretoSpider(scrapy.Spider):
    name = 'tesouro-direto'
    allowed_domains = ['fazenda.gov.br']
    start_urls = ['http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos']

    def parse(self, response):
    
        all_fields = response.xpath("//tr[contains(@class, 'camposTesouroDireto')]")
        
        for field in all_fields:
        	yield {
            	'Line': field.xpath('td/text()').extract()
            }