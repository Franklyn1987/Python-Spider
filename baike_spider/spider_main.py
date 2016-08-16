# coding=utf-8
import html_downloader, html_parser, url_manager, html_outputer


class SpiderMain:
    def __init__(self):
        self.urlManager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        self.urlManager.add_new_url(url)
        count = 1
        while self.urlManager.has_new_url():  # 当有新的带爬取的url
            try:
                newUrl = self.urlManager.get_new_url()  # 取一个新的url
                html_cont = self.downloader.download(newUrl)  # 下载爬取得网页页面
                print "craw %d : %s" % (count, newUrl)
                newUrls, newData = self.parser.parse(newUrl, html_cont)  # 对下载好的网页进行解析,得到新的url(可能不止一个)和数据
                self.urlManager.add_new_urls(newUrls)  # 将新得到的urls添加到url管理器中
                self.outputer.collectData(newData)  # 同时对得到的数据进行收集

                if count == 1000:
                    break
                count += 1
            except:
                print 'craw failed'
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
