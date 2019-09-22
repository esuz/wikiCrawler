import requests
from bs4 import BeautifulSoup

class Page(object):

    def __init__(self, url):
        self.url = url
        self.summary = None
        self.website = requests.get(self.url).text

    def _clean_links(self, links):
        cleaned_links = []
        for i in links:
            if isinstance(i, str):
                cleaned_links.append(i)
        return(cleaned_links)

    def _select_wiki_links(self, links):
        valid_links = []
        import re
        pattern_wiki = re.compile("^/wiki/.*")
        pattern_dots = re.compile(".*[:\.#].*")
        for c in links:
            if pattern_wiki.match(c) and not pattern_dots.match(c):
                valid_links.append(c)
        return valid_links

    def summarize(self):
        soup = BeautifulSoup(self.website, "lxml")
        soup_body = soup.body

        candidate_links = []
        for link in soup_body.find_all('a'):
            candidate_links.append(link.get('href'))

        candidate_links = self._clean_links(candidate_links)
        links = self._select_wiki_links(candidate_links)

        summary = {"url": self.url, "link_num": len(links), "links": links}
        self.summary = summary
        return(summary)

    def harvest_html(self):
        return(self.website)
