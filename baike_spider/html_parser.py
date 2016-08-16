# coding=utf-8

import urlparse, re
from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self):
        pass

    def parse(self, base_url, html_cont):
        if base_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(base_url, soup)
        new_data = self.get_new_data(base_url, soup)
        return new_urls, new_data

    def get_new_urls(self, base_url, soup):

        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(base_url, new_url)
            new_urls.add(new_full_url)

        return new_urls  # 获取当前页面中所有新的url

    def get_new_data(self, page_url, soup):

        res_data = {'url': page_url}
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')  # 寻找在dd标签下的h1子标签,通过两个find方法来获取
        res_data['title_node'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary_node'] = summary_node.get_text()

        return res_data
