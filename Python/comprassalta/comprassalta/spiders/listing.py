import scrapy
import re
from comprassalta.items import ComprassaltaItem


class ListingSpider(scrapy.Spider):
    name = 'listing'
    allowed_domains = ['compras.salta.gov.ar']
    start_urls = ['http://compras.salta.gov.ar/publico/publicacionactual/panelfiltrobusqueda/0']

    def parse(self, response):
        item = ComprassaltaItem()
        notices = response.css("#publicacionFiltro > article")

        # Looping through notices
        for notice in notices:
            item['title'] = notice.css('div.publicacion-cuerpo > div:nth-child(1) > span.publicacion-fila-descripcion::text').get()
            item['entityIdAtSource'] = "".join(re.findall("[0-9/]", notice.css('div.media > div > span:nth-child(2)::text').get()))
            item['shortDescription'] = re.split(':', notice.css('div.publicacion-cuerpo > div:nth-child(4) > span.publicacion-fila-descripcion::text').get())[-1]
            item['supplierName'] = notice.css('div.publicacion-cuerpo > div:nth-child(2) > span.publicacion-fila-descripcion::text').get()
            item['openDate'] = notice.css('div.media > div > span:nth-child(1) > span:nth-child(2)::text').get()
            item['originalUrl'] = "http://compras.salta.gov.ar" + eval(re.split('=', notice.css('div.publicacion-cuerpo input::attr(onclick)').get())[-1])
            yield item

        # Checking for next page, if page exists it will move to next page
        next_page = response.css('#publicacionFiltro > div.pagination > a:nth-last-child(2)::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)




