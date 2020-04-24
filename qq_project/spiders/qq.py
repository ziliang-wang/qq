import json
import time
import scrapy
from qq_project.items import QqProjectItem
from selenium import webdriver


class QqSpider(scrapy.Spider):
    
    name = 'qq'
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI45895470497458923&g_' \
          'tk=5381&sign=zza8j7jk883cwdj5a1a372d1703451366208400d2f70fd04&loginUin=0' \
          '&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=' \
          'yqq.json&needNewCode=0&data=%7B%22detail%22%3A%7B%22module%22%3A%22musicToplist.' \
          'ToplistInfoServer%22%2C%22method%22%3A%22GetDetail%22%2C%22param%22%3A%7B%22' \
          'topId%22%3A4%2C%22offset%22%3A0%2C%22num%22%3A20%2C%22period%22%3A%222020-' \
          '04-24%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'

    def start_requests(self):
        yield scrapy.Request(self.url)

    def parse(self, response):
        item = QqProjectItem()
        detail = json.loads(response.text)['detail']
        item_list = []
        for song in detail['data']['data']['song']:
            item['rank'] = song['rank']
            item['title'] = song['title']
            item['singer'] = song['singerName']
            item['time'] = '00:00'
            item_list.append(dict(item))

        driver = webdriver.PhantomJS()
        driver.get('https://y.qq.com/n/yqq/toplist/4.html')
        time.sleep(3)

        for idx in range(len(item_list)):
            xpath = '//ul[@class="songlist__list"]/li[{}]/div/div[last()-1]'.format(idx+1)
            item_list[idx]['time'] = driver.find_element_by_xpath(xpath).text
            yield item_list[idx]
        driver.close()






