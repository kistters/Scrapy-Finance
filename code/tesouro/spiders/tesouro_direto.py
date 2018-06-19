# -*- coding: utf-8 -*-
import scrapy


class TesouroDiretoSpider(scrapy.Spider):
	name = 'tesouro-direto'
	allowed_domains = ['fazenda.gov.br']
	start_urls = ['http://www.tesouro.fazenda.gov.br/tesouro-direto-precos-e-taxas-dos-titulos']

	def parse(self, response):

		all_fields = response.xpath("//tr[contains(@class, 'camposTesouroDireto')]")

		for field in all_fields:

			line = field.xpath('td/text()').extract()

			if len(line) == 5:
				yield {
					'Type':'investir',
					'Title': line[0], 
					'ExpirationDate': line[1], 
					'Tax': line[2], 
					'MinimalValue': line[3],
					'UnitPrice': line[4],
				}

			if len(line) == 4:
				yield {
					'Type':'resgatar',
					'Title': line[0], 
					'ExpirationDate': line[1], 
					'Tax': line[2], 
					'UnitPrice': line[3] 
				}