import scrapy
import pymysql
import random
from scrapy import Request
from collector.settings import MySQLDBConfig


class TestrandomproxySpider(scrapy.Spider):
    name = 'testRandomProxy'
    allowed_domains = ["httpbin.org/ip"]

    def __init__(self):
        self.db = pymysql.connect(**MySQLDBConfig)
        self.proxyList = []
        cursor = self.db.cursor()
        sqlIps = "SELECT ip FROM ips"
        ips = cursor.execute(sqlIps)
        results = cursor.fetchall()
        print(results)
        for ip in results:
            self.proxyList.append(ip[0])
        """
        chromeOptions = Options()
        proxy = random.choice(self.proxyList)
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument(f"--proxy-server={proxy}")
        self.chrome = webdriver.Chrome(
            chrome_options=chromeOptions, executable_path=ChromeDriverManager().install())
        """

    def start_requests(self):
        for i in range(5):
            try:
                response = scrapy.Request(
                    "https://httpbin.org/ip", callback=self.parse, dont_filter=True, meta={"proxy": random.choice(self.proxyList)})
                yield response
            except Exception:
                print("Invalid Proxy IP!")

    def parse(self, response):
        print(f"response.text: {response.text}")
