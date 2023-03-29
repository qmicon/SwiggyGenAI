import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
time.sleep(10)
crawler.search_suggest("Pizza")
crawler.search("Pizza", "Restaurant")
for element in crawler.search_elements:
    print(crawler.parse_search_restaurant(element))
time.sleep(20)