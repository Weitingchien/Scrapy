import scrapy
import random
import time
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YtchannelSpider(scrapy.Spider):
    name = "ytChannel"
    allowed_domains = ["www.youtube.com"]
    # start_urls = ["https://www.youtube.com/"]

    def start_requests(self):
        urls = ["https://www.youtube.com/channel/UCmreSJkj5C2L3BpJsZ7ikvQ/videos",
                "https://www.youtube.com/c/SellyTwitch/videos"]
        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=random.uniform(5, 10), wait_until=EC.presence_of_element_located((By.ID, "page-manager")))

    def parse(self, response):
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print("===========================================")
        print(response.text)
        time.sleep(20)
        videosTitle = response.css(
            "h3.ytd-grid-video-renderer a::text").get()
        videosLink = response.css(
            "h3.ytd-grid-video-renderer a::attr(href)").get()
        videosImage = response.css(
            "ytd-thumbnail.ytd-grid-video-renderer yt-img-shadow.ytd-thumbnail img::attr(src)").get()
        videosStatus = response.css(
            "ytd-thumbnail-overlay-time-status-renderer.ytd-thumbnail::attr(overlay-style)").get()
        videosChannelName = response.css(
            "yt-formatted-string.ytd-channel-name::text").get()
        metaData = response.css(
            "div.ytd-grid-video-renderer span.ytd-grid-video-renderer::text").getall()

        videoLinkParse = videosLink.split("=", 1)
        videosID = videoLinkParse[1]

        videosViews = None
        videosUploadedTime = None

        for i in range(len(metaData)):
            if i < 1:
                videosViews = metaData[i]
                videosUploadedTime = metaData[i+1]
        videoItem = {
            "videoID": videosID,
            "videoTitle": videosTitle,
            "videoLink": f"https://www.youtube.com{videosLink}",
            "videoImage": videosImage,
            "videoStatus": videosStatus,
            "videoViews": videosViews,
            "videoChannelName": videosChannelName,
            "videoUploadedTime": videosUploadedTime
        }
        print(f"videoItem: {videoItem}")

        yield videoItem
