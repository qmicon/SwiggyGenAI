import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
crawler.search_suggest("KFC")
time.sleep(20)