import scrapy
from ..items import BlogsItem

class blogSpider(scrapy.Spider):
    name = 'blog'
    next_page = 2
    start_urls = [#'https://machinelearningmastery.com/blog/',
                    'https://machinelearningmastery.com/blog/page/1/']
    

    def parse(self, response):
        title = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entry-title", " " ))]//a//text()').extract()
        link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "entry-title", " " ))]//a/@href').extract()
        updated_on = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "updated", " " ))]//text()').extract()
        author = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fn", " " ))]//a//text()').extract()
        content = response.xpath('//p//text()').extract()

        #len = len(title)
        for i in range(len(title)):
            blogItems = BlogsItem()
            blogItems['title'] = title[i]
            blogItems['link'] = link[i]
            blogItems['updated_on'] = updated_on[i]
            blogItems['author'] = author[i]
            blogItems['content'] = content[i]
            yield blogItems

        next_page_url = 'https://machinelearningmastery.com/blog/page/'+ str(blogSpider.next_page) +'/'
        if blogSpider.next_page < 85:
            blogSpider.next_page += 1
            yield response.follow(next_page_url, callback = self.parse )
            '''
            yield {'title': title,
                'updated_on': updated_on,
                'author': author,
                'content': content
                }
            '''            