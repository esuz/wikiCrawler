import requests
from bs4 import BeautifulSoup

class Page(object):

    """
    Page class providing functions to access information on webpage
    using BeautifulSoup. Functionalities include the gathering of
    /wiki/.* links from a given wikipedia website. Currently german
    wikipedia pages is hardcoded in the crawler class.
    """

    def __init__(self, url: str):
        """Initializes class with url.

        Args:
            url(str): URL e.g. "https://de.wikipedia.org/wiki/Konrad_Zuse"

        Example:
            >>> url = "https://de.wikipedia.org/wiki/Konrad_Zuse"
            >>> page = Page(url)
            >>> page_summary = page.summarize()
        """
        self.url = url
        self.summary = None
        self.website = requests.get(self.url).text

    def _clean_links(self, links:list) -> list:
        """Removing None from link list; keeping only strings

        Args:
            links (list): List of links (str)

        Returns:
            cleaned_links (list)
        """
        cleaned_links = []
        for i in links:
            if isinstance(i, str):
                cleaned_links.append(i)
        return(cleaned_links)

    def _select_wiki_links(self, links: list) -> list:
        """Selecting only valid wikipedia links.
        and removing image or any other /wiki/Datei:.* links

        Args:
            links (list): List of links (str)

        Returns:
            cleaned_links (list)
        """
        valid_links = []
        import re
        pattern_wiki = re.compile("^/wiki/.*")
        pattern_dots = re.compile(".*[:\.#].*")
        for c in links:
            if pattern_wiki.match(c) and not pattern_dots.match(c):
                valid_links.append(c)
        return valid_links

    def summarize(self) -> dict:
        """Generates summary of wikipedia page.

        Returns:
            summary (dict): {"url": url, "link_num": len(links), "links": links}

        """
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
        """
        Returns:
             HTML of webpage.
        """
        return(self.website)
