import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
crawler.search_suggest("Chicken")
crawler.search("Chic")
time.sleep(20)