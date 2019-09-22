from .page import Page

class Crawler(object):
    def __init__(self, depth=20, time=1, threads=1):
        self.depth = depth
        self.time = time
        self.thread = threads
        page_trail = {}
        for i in range(threads):
            page_trail.update({'thread_' + str(i):[]})


    def _build_url(self, page):
        link_num = page.summary["link_num"]
        links = page.summary["links"]
        if link_num > 0:
            import random
            #random.seed(20190922)
            randint = random.randint(1, link_num - 1)
            prefix = "https://de.wikipedia.org"
            postfix = links[randint]
            return prefix + postfix
        else:
            print("No links on page.")
            return

    def crawl_randomly(self, page):
        depth = self.depth

        for i in range(depth):
            import time
            time.sleep(self.time)

            url = self._build_url(page)
            print(url)
            page = Page(url)
            page.summarize()

    def crawl_randomly_mt(self, page):
        pass