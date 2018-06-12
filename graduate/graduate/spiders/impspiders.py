#-*-coding utf-8-*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import InvestmentItem

class InvestmentSpider(scrapy.Spider):
    name = "investment"

    start_urls = ["http://www.tmtpost.com/tag/299045"]

    def parse(self, response):
        #提取列表中每一个新闻的链接
        #le = LinkExtractor(restrict_css='ul#articleList>li>h3')

        #for link in le.extract_links(response):
            #yield scrapy.Request(link.url, callback=self.parse_investment())

        link = response.css('div.cont h2 a[target=_blank]::attr(href)').extract()
        print(link)
        for one in link:
            url = response.urljoin(one)

            yield scrapy.Request(url=url, callback=self.parse_investment)

        for num in range(1, 27):
            next_link = "http://www.tmtpost.com/tag/299045/"
            next_link += str(num)
            print(next_link)
            yield scrapy.Request(url=next_link, callback=self.parse)

        #提取下一页
        # le = LinkExtractor(restrict_css='li.page+li.page-rl>a::attr[href]')
        # links = le.extract_links(response)
        # print(links)
        # if links:
        #     next_url = links[-1].url
        #     print(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

    def parse_investment(self, response):
        item = InvestmentItem()

        item['title'] = response.xpath('//article/h1/text()').extract_first()

        item['date'] = response.xpath('//article/div[@class="post-info"]/span[@class="time "]/text()').extract_first()

        item['content'] = response.xpath('string(//div[@class="inner"])').extract_first()
        item['source'] = response.xpath('//article/div[@class="post-info"]/a/text()').extract_first()
        item['link'] = response.url


        yield item


    # def parse(self, response):
    #     for book in response.css('article.product_pod'):
    #         name = book.xpath('./h3/a/@title').extract_first()
    #         price = book.css('p.price_color::text').extract_first()
    #         yield{
    #             'name': name,
    #             'price': price,
    #         }
    #     #提取链接
    #     next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
    #     print(next_url)
    #     if next_url:
    #         next_url = response.urljoin(next_url)
    #         yield scrapy.Request(next_url, callback=self.parse)
    #     #
    #     # le = LinkExtractor(restrict_css='ul.pager li.next')
    #     # links = le.extract_links(response)
    #     # if links:
    #     #     next_url = links[0].url
    #     #     yield scrapy.Request(next_url, callback=self.parse)