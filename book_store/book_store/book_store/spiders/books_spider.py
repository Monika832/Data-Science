# creating our spider
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    # allows us to make GET/POST request to a particular url
    def start_requests(self):
        # here we give the list of urls from which we want to scrape the data
        urls = [
            'http://books.toscrape.com/'
        ]
        # generator function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # we make a request on this url and when the response comes, we need to parse that response

    # parse method knows what to do with the particular response
    def parse(self, response):
        # PARSED RESPONSE FROM THE FIRST PAGE
        # parse the response (all the quotes in a page) and save it in a JSON format
        for q in response.css("article.product_pod"):
            image_url = q.css('a img::attr(src)').get()
            book_title = q.css('a img::attr(alt)').get()
            product_price = q.css('div p.price_color::text').get()

             # yield this in the form of a dictionary
            yield {
                'image_url': image_url,
                'book_title': book_title,
                'product_price': product_price
            }
        
        # check if there is a next page or not
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)