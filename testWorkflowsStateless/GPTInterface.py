import sys
import time

sys.path.append('..')

from SwiggyCrawlerStateless import SwiggyCrawlerStateless

crawler = SwiggyCrawlerStateless()
time.sleep(10)
# GPT reads the objective and searches Pizza
# Action search["Pizza", "Restaurant"]
search_suggest_elements = crawler.search_suggest("Pizza")
search_elements = crawler.search(search_suggest_elements, "Pizza", "Restaurant")
if not search_elements:
    exit()

print("Search Results")
output = crawler.render_search_restaurants(search_elements)
print(output)
# GPT reads the search results and chooses the restaurant at index 2
# Action click[2]
menu_elements = crawler.search_restaurant_by_index(search_elements, 2)

print("Menu Items")
output = crawler.render_menu_items(menu_elements)
print(output)
# GPT looks at the menu items and chooses to order two index 143
# Action add[143, 2]
crawler.add_menu_item_by_index_x_times(menu_elements, 143, 2)

# Action checkout
crawler.checkout()
time.sleep(20)