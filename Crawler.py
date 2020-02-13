import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    urls = ['http://brickset.com/sets/year-2016']

    def parse(self,response):
        set_selector = '.set'
        for brickset in response.css(set_selector):
            name_selector = 'h1 ::text'
            piece_selector = './/d1[dt/text()="Pieces"]/dd/a/text()'
            minifigs_selector = './/d1[dt/text()="Minifigs"]/dd/a/text()'
            img_selector = 'img ::attr(src)'
            yield{
                    'name' : brickset.css(name_selector).extract_first(),
                    'pieces' : brickset.xpath(piece_selector).extract_first(),
                    'minifigs' : brickset.xpath(minifigs_selector).extract_first(),
                    'image' : brickset.css(img_selector).extract_first(),
                }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
