"""
import scrapy


class TestrandomproxySpider(scrapy.Spider):
    name = 'testRandomProxy'
    allowed_domains = ["httpbin.org/ip"]

    def start_requests(self):
        for i in range(5):
            try:
                yield scrapy.Request(
                    "https://httpbin.org/ip", callback=self.parse, dont_filter=True)
            except Exception:
                print("Invalid Proxy IP!")

    def parse(self, response):
        print(f"response.text: {response.text}")
        print(f"user-agent: {response.request.headers['User-Agent']}")

    # Here we pass proxy in "scrapy.Request()" but we define in the middleware made code structure clear
    def start_requests(self):
        for i in range(5):
            try:
                response = scrapy.Request(
                    "https://httpbin.org/ip", callback=self.parse, dont_filter=True, meta={"proxy": random.choice(self.proxyList)})
                yield response
            except Exception:
                print("Invalid Proxy IP!")
    
"""
