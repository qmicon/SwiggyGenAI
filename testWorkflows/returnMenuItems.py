import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
time.sleep(10)
crawler.search_suggest("Pizza")
crawler.search("Pizza", "Restaurant")
crawler.filter_by_restaurant(3.5, 40)
for element in crawler.menu_elements:
    print(crawler.parse_menu_element(element))
time.sleep(20)