import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
time.sleep(10)
crawler.search_suggest("Pizza")
crawler.search("Pizza", "Restaurant")
crawler.filter_by_restaurant(3.5, 40)
crawler.add_and_checkout_menu_items(['Coca Cola (250 Ml)', '8" Small Tuscan Spicy Tomato'])
time.sleep(20)