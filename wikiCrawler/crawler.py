from .page import Page
import threading
from concurrent.futures import ThreadPoolExecutor

class Crawler(object):
    """ Wikipedia crawler.

    Jumps from wikipedia page to wikipedia page based on
    random choice of valid wikipedia links of current page.
    Features inlcude multithreaded implementation.
    """
    def __init__(self, depth=20, time=1, threads=1):
        """Initialises crawler.

        Args:
            depth (int): depth to crawl
            time (int): time (secs) to wait between each website change
            threads (int): how many crawlers to spawn
        """
        self.depth = depth
        self.time = time
        self.threads = threads
        page_trail = {}
        for i in range(threads):
            page_trail.update({'thread_' + str(i):[]})


    def _build_url(self, page: Page) -> str:
        """ Choices random url based on options supplied in page object.

        Args:
            Page (page): Page object.

        Returns:
            url (str): prefix + postfix.
        """
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

    def _crawl_randomly(self, page, threads):
        depth = self.depth
        #print("Task Executed {}".format(threading.current_thread()))
        for i in range(depth):
            import time
            time.sleep(self.time)

            url = self._build_url(page)
            print("Thread "+ str(threads) + ":" + url)
            page = Page(url)
            page.summarize()

    def crawl_randomly(self, page, threads):
        self.threads = threads
        from itertools import repeat
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            future = executor.map(self._crawl_randomly, repeat(page), range(self.threads))