import scrapy
from election_offices.items import ElectionOfficesItem


class ElectionOfficeSpider(scrapy.Spider):
    name = 'ElectionOfficeSpider'
    start_urls = ['http://www.aboutmyvote.co.uk/register-to-vote/find-your-local-authority']

    def chunker(self, seq, size):
        return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

    def parse(self, response):
        for url in response.xpath('/html/body/div/main/div/div/div[2]/div[3]/div/div[2]/a/@href'):
            yield scrapy.Request(url.extract(), self.parse_eo)

    def parse_eo(self, response):
        eo_list = response.xpath('//div[contains(@id, "content_div_")]/div/p')
        # Fix bromsgrove
        if len(eo_list) % 2 == 0:
            for eo in self.chunker(eo_list, 2):
                item = ElectionOfficesItem()
                item['name'] = eo[0].xpath('b/text()').extract()
                item['address'] = eo[1].xpath("text()").extract()
                item['email'] = eo[1].xpath("a/text()").extract()
                yield item
        else:
            # Fix 'B' page as it has an error currently.
            pass
