from wikiCrawler.page import Page
from wikiCrawler.crawler import Crawler

url = 'https://de.wikipedia.org/wiki/Konrad_Zuse'

page = Page(url)
page.summarize()
page.harvest_html()

crawler = Crawler(depth=10)
crawler.crawl_randomly(page)

