import scrapy

from cubeecraft.items import CubeecraftItem


class CubeeImageScrap(scrapy.Spider):
    name = 'cubeecraft'
    start_urls = ['https://www.cubeecraft.com/cubees']

    def parse(self, response, **kwargs):
        for cubee in response.css('li.cubee-column-thumbnail-wrapper '):
            cubee_link = cubee.css('a').attrib['href']
            yield response.follow(cubee_link, self.parse_cubee)
        for next_page in response.css("span.next a::attr(href)"):
            yield response.follow(next_page, self.parse)

    def parse_cubee(self, response):
        cubee_name = response.css('h3.underlined-header::text').get().strip().title()
        cubee_image_link = response.xpath('/html/body/div/div[1]/main/div/div[2]/div[1]/img').xpath("@src").get()
        item = CubeecraftItem()
        item['image_urls'] = [cubee_image_link]
        item['image_name'] = cubee_name
        yield item