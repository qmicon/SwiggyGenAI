import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
crawler.search_suggest("Chicken")
for element in crawler.search_suggest_elements:
    print(crawler.parse_search_suggest(element))
time.sleep(20)