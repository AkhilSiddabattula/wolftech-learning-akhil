import scrapy


class ScrapeSpider(scrapy.Spider):
    name = 'scrape'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        quotes = response.css('div.quote')
        for quote in quotes:
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a::text').getall()
            }


