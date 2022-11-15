import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['magnatiles.com']
    start_urls = ['https://www.magnatiles.com/products/']

    def parse(self, response):
        image_urls = response.css('img.attachment-woocommerce_thumbnail.size-woocommerce_thumbnail::attr(src)').getall()

        yield {
            'image_urls': image_urls
        }
