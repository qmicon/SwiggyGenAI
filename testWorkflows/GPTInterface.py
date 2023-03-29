import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
time.sleep(10)
# GPT reads the objective and searches Pizza
crawler.search_suggest("Pizza")
print("Search Suggestions")
output = crawler.render_search_suggestions()
print(output)
# GPT reads the search suggestions and chooses the suggestion at index 4
category = crawler.search_suggestion_by_index(4)
if category != 'Restaurant':
    exit()
print("Search Results")
output = crawler.render_search_restaurants()
print(output)
# GPT reads the search results and chooses the restaurant at index 2
check = crawler.search_restaurant_by_index(2)
if not check:
    exit()
print("Menu Items")
output = crawler.render_menu_items()
print(output)
# GPT looks at the menu items and chooses to order index 0 and 5
crawler.add_and_checkout_menu_items_by_index([6, 7])
time.sleep(20)

'''
Search Suggestions

id: 0, name: Pizza, category: Dish

id: 1, name: Domino's Pizza, category: Restaurant

id: 2, name: Pizza Hut, category: Restaurant

id: 3, name: La Pino'z Pizza, category: Restaurant

id: 4, name: Oven Story Pizza, category: Restaurant

id: 5, name: The Pizza Bakery, category: Restaurant

id: 6, name: MOJO Pizza - 2X Toppings, category: Restaurant

id: 7, name: Margherita Pizza, category: Dish

id: 8, name: Farm House Pizza, category: Dish

id: 9, name: Veg Pizza Mcpuff, category: Dish

Search Results: Oven Story Pizza

id: 0, name:  Crusto's - Cheese Burst Pizza,  status: Open

id: 1, name:  Crusto's - Cheese Burst Pizza,  status: Open

id: 2, name:  Pizza Hut,  status: Open

id: 3, name:  Pizza Corner,  status: Open

id: 4, name:  Olio - The Wood Fired Pizzeria,  status: Open

id: 5, name:  Pizza Paradise,  status: Open

id: 6, name:  Oven Theory Pizza - OTP,  status: Open

id: 7, name:  Yumlane Pizza,  status: Open

id: 8, name:  Pizza Party,  status: Open

id: 9, name:  WoodFire Pizza House,  status: Open

id: 10, name:  THE PIZZA FOLKS,  status: Open

id: 11, name:  Joey's Pizza Express Delivery,  status: Open

id: 12, name:  crunch pizza express delivery,  status: Open

id: 13, name:  Nomad Pizza- Traveller Series,  status: Open

id: 14, name:  Pizza O'Clock,  status: Open

id: 15, name:  Midnight Rascals Pizza - MRP,  status: Open

id: 16, name:  Baking Bad  - Pizza Delivery,  status: Open

id: 17, name:  The Firewood Pizza,  status: Open

id: 18, name:  Wood Fire Pizza,  status: Open

id: 19, name:  Pasta & Pizza,  status: Open

id: 20, name:  Pizza Theatre,  status: Open

id: 21, name:  pizza & Burger,  status: Open

id: 22, name:  Deshi Fusion Pizza,  status: Open

id: 23, name:  Pizza Kitchen,  status: Open

id: 24, name:  Pizza Kingdom,  status: Open

id: 25, name:  Pizza Box,  status: Open

id: 26, name:  Nomad - Vegetarian and Plant based Pizza Series,  status: Open

id: 27, name:  Scooby Cookhouse,  status: Open

id: 28, name:  Italian BOB Pizza's,  status: Open

id: 29, name:  Burger & Wings,  status: Open

id: 30, name:  Midnight Pizza And Food,  status: Open

id: 31, name:  Kilo Paradise Biriyani,  status: Open

id: 32, name:  Khan Sahab,  status: Open

id: 33, name:  Beyond The Crust - BTC,  status: Open

id: 34, name:  Bites more,  status: Open

id: 35, name:  Burger Eat,  status: Open

id: 36, name:  Biryani @Rs.99 Only,  status: Open

id: 37, name:  Thalis , Bowls & More,  status: Open

id: 38, name:  Hungry Burger,  status: Open

id: 39, name:  Hunger Kings,  status: Open

id: 40, name:  Rs 99 Only,  status: Open

id: 41, name:  Fresh food Eat,  status: Open

id: 42, name:  Eat Food,  status: Open

id: 43, name:  Rana vada pav,  status: Open

id: 44, name:  Biryani Box,  status: Open

id: 45, name:  Kouzina Kafe - The Food Court,  status: Open

id: 46, name:  limelight-Royal Orchid Hotel,  status: Open

id: 47, name:  Hyderabadi Suchi Biryani,  status: Open

id: 48, name:  Bawarchi Biryanis,  status: Open

id: 49, name:  Rayalaseema'S Amigos,  status: Open

id: 50, name:  The Icecream Zone,  status: Open

id: 51, name:  Foodpecker,  status: Open

id: 52, name:  Ayaansh Foods,  status: Open

id: 53, name:  Ember & Frost,  status: Open

Menu Items: Pizza Hut

id: 0, name:  Super Value Deal : 2 Medium Veg Pizzas starting at Rs 649 (Save Upto 41%) customizable: True

id: 1, name:  Super Value Deal : 2 Medium Veg San Francisco Style Pizzas starting at Rs 649 (Save Upto 41%) customizable: True

id: 2, name:  Super Value Deal : 2 Medium Non -Veg Pizzas starting at Rs 749 (Save Upto 39%) customizable: True

id: 3, name:  Super Value Deal : 2 Medium Non-Veg San Francisco Style Pizzas starting at Rs 749 (Save Upto 39%) customizable: True

id: 4, name:  Cheesy Momo Mia Pizza Veg customizable: True

id: 5, name:  Cheesy Momo Mia Pizza Non Veg customizable: True

id: 6, name:  So Cheesy Baked Momos Veg customizable: False

id: 7, name:  So Cheesy Baked Momos Non Veg customizable: False

id: 8, name:  Margherita customizable: True

id: 9, name:  Veggie Feast customizable: True

id: 10, name:  Double Cheese customizable: True

id: 11, name:  Tandoori Paneer customizable: True

id: 12, name:  Country Feast customizable: True

id: 13, name:  Veggie Supreme customizable: True

id: 14, name:  Veg Exotica customizable: True

id: 15, name:  Chicken Tikka customizable: True

id: 16, name:  Triple Chicken Feast customizable: True

id: 17, name:  Chicken Supreme customizable: True

id: 18, name:  Garlic Bread Stix customizable: False

id: 19, name:  Garlic Bread Spicy Supreme customizable: False

id: 20, name:  Create Your Flavour Fun Combo - Box Of 4 - Veg customizable: True

id: 21, name:  Chicken Supreme customizable: True

id: 22, name:  My Box - Veg customizable: True

id: 23, name:  Choco Volcano customizable: False

id: 24, name:  Super Value Deal : 2 Medium Veg Pizzas starting at Rs 649 (Save Upto 41%) customizable: True

id: 25, name:  Super Value Deal : 2 Medium Veg San Francisco Style Pizzas starting at Rs 649 (Save Upto 41%) customizable: True

id: 26, name:  Super Value Deal : 2 Medium Non -Veg Pizzas starting at Rs 749 (Save Upto 39%) customizable: True

id: 27, name:  Super Value Deal : 2 Medium Non-Veg San Francisco Style Pizzas starting at Rs 749 (Save Upto 39%) customizable: True

id: 28, name:  Cheese Maxx Veggie Feast customizable: True

id: 29, name:  Cheese Maxx Veggie Supreme customizable: True

id: 30, name:  Cheese Maxx Country Feast customizable: True

id: 31, name:  Cheese Maxx Chicken Tikka customizable: True

id: 32, name:  Cheese Maxx Chicken Supreme customizable: True

id: 33, name:  Cheesy Momo Mia Pizza Veg customizable: True

id: 34, name:  Cheesy Momo Mia Pizza Non Veg customizable: True

id: 35, name:  So Cheesy Baked Momos Veg customizable: False

id: 36, name:  So Cheesy Baked Momos Non Veg customizable: False

id: 37, name:  Momo Dip customizable: False

id: 38, name:  Schezwan Margherita customizable: True

id: 39, name:  Margherita customizable: True

id: 40, name:  Tandoori Onion customizable: True

id: 41, name:  Corn & Cheese customizable: True

id: 42, name:  Veggie Tandoori customizable: True

id: 43, name:  Spiced Paneer customizable: True

id: 44, name:  Veggie Feast customizable: True

id: 45, name:  Double Cheese customizable: True

id: 46, name:  Veggie Lover customizable: True

id: 47, name:  Tandoori Paneer customizable: True

id: 48, name:  Farmers Pick customizable: True

id: 49, name:  Country Feast customizable: True

id: 50, name:  Veg Kebab Surprise customizable: True

id: 51, name:  Veggie Supreme customizable: True

id: 52, name:  Veg Exotica customizable: True

id: 53, name:  Double Paneer Supreme customizable: True

id: 54, name:  Margherita Pizza customizable: False

id: 55, name:  Sizzling Schezwan Chicken customizable: True

id: 56, name:  Chicken Sausage customizable: True

id: 57, name:  Spiced Chicken Meatballs customizable: True

id: 58, name:  Double Chicken Sausage customizable: True

id: 59, name:  Chicken N Corn Delight customizable: True

id: 60, name:  Chicken Pepperoni customizable: True

id: 61, name:  Malai Chicken Tikka customizable: True

id: 62, name:  Chicken Tikka customizable: True

id: 63, name:  Chicken Pepper Crunch customizable: True

id: 64, name:  Italian Chicken Feast customizable: True

id: 65, name:  Triple Chicken Feast customizable: True

id: 66, name:  Chicken Tikka Supreme customizable: True

id: 67, name:  Chicken Supreme customizable: True

id: 68, name:  NEW Garlic Breadstix & Pepsi Combo customizable: False      

id: 69, name:  Cheese Garlic Bread customizable: False

id: 70, name:  Garlic Bread Stix customizable: False

id: 71, name:  Garlic Bread Spicy Supreme customizable: False

id: 72, name:  Creamy Garlic Breadstix customizable: False

id: 73, name:  Mexican Garlic Breadstix customizable: False

id: 74, name:  Create Your Flavour Fun Combo - Box Of 4 - Veg customizable: True

id: 75, name:  Create Your Flavour Fun Combo - Box Of 4 - Non Veg customizable: True

id: 76, name:  Create Your Flavour Fun Combo - Box Of 2 - Veg Pizza customizable: True

id: 77, name:  Create Your Flavour Fun Combo - Box Of 2 - Non Veg Pizza customizable: True

id: 78, name:  Classic Veg Combo customizable: False

id: 79, name:  Schezwan Veg Combo customizable: False

id: 80, name:  Tandoori Classic Veg Combo customizable: False

id: 81, name:  Cheesy Classic Veg Combo customizable: False

id: 82, name:  Tandoori Classic Non-Veg Combo customizable: False

id: 83, name:  Italian Schezwan Non-Veg Combo customizable: False

id: 84, name:  Classic Corn - New customizable: True

id: 85, name:  Classic Onion Capsicum - New customizable: True

id: 86, name:  Italian Onion Tomato - New customizable: True

id: 87, name:  Tandoori Mushroom & Sweet Corn - New customizable: True     

id: 88, name:  Schezwan Corn & Capsicum - New customizable: True

id: 89, name:  Only Cheesy - New customizable: True

id: 90, name:  Classic Paneer, Capsicum & Onion - New customizable: True   

id: 91, name:  Classic Sausage - New customizable: True

id: 92, name:  Italian Pepperoni & Onion - New customizable: True

id: 93, name:  Schezwan Meatball & Capsicum - New customizable: True       

id: 94, name:  Tandoori Tikka & Onion - New customizable: True

id: 95, name:  Classic Loaded Chicken Delight - New customizable: True     

id: 96, name:  Margherita customizable: True

id: 97, name:  Spiced Paneer customizable: True

id: 98, name:  Veg Kebab Surprise customizable: True

id: 99, name:  Veggie Supreme customizable: True

id: 100, name:  Double Paneer Supreme customizable: True

id: 101, name:  Chicken Pepperoni customizable: True

id: 102, name:  Chicken Supreme customizable: True

id: 103, name:  San Francisco Style My Box Veg customizable: True

id: 104, name:  San Francisco Style My Box Non Veg customizable: True      

id: 105, name:  San Francisco Style Hut Treat Meal for 2 Veg customizable: 
True

id: 106, name:  San Francisco Style Hut Treat Meal for 2 Non Veg customizable: True

id: 107, name:  San Francisco Style Hut Treat Meal for 4 Veg @ 859 customizable: True

id: 108, name:  San Francisco Style Hut Treat Meal for 4 Non Veg @ 959 customizable: True

id: 109, name:  San Francisco Style Hut Treat Meal for 4 Veg @ 959 customizable: True

id: 110, name:  San Francisco Style Hut Treat Meal for 4 Non Veg @ 1069 customizable: True

id: 111, name:  My Box - Veg customizable: True

id: 112, name:  My Box - Non Veg customizable: True

id: 113, name:  My Box Pasta - Veg customizable: True

id: 114, name:  My Box with Choco Sundae - Veg customizable: True

id: 115, name:  My Box Pasta - Non Veg customizable: True

id: 116, name:  My Box with Choco Sundae - Non Veg customizable: True      

id: 117, name:  Hut Treat Meal for 2 - Veg customizable: True

id: 118, name:  Hut Treat Meal for 2 - Non Veg customizable: True

id: 119, name:  Hut Treat Meal for 4 - Veg @859 customizable: True

id: 120, name:  Hut Treat Meal for 4 - Veg @959 customizable: True

id: 121, name:  Hut Treat Meal for 4 - Non Veg @959 customizable: True     

id: 122, name:  Hut Treat Meal for 4 - Non Veg @1069 customizable: True    

id: 123, name:  Creamy Mushroom Pasta customizable: False

id: 124, name:  Cheesy Comfort customizable: False

id: 125, name:  Cheesy Comfort - Non Veg customizable: False

id: 126, name:  Spiced Tomato Twist Veg customizable: False

id: 127, name:  Spiced Tomato Twist Non Veg customizable: False

id: 128, name:  Indi Rockin Roll Veg customizable: False

id: 129, name:  Zesty Paneer Pocket customizable: False

id: 130, name:  Jalapeno Poppers customizable: False

id: 131, name:  Potato Poppers customizable: False

id: 132, name:  Veg Mayonnaise Dip customizable: False

id: 133, name:  Cheesy Dip customizable: False

id: 134, name:  Ketchup customizable: False

id: 135, name:  Spicy Baked Chicken Wings customizable: False

id: 136, name:  Spicy Baked Chicken Wings (4 pcs) customizable: False      

id: 137, name:  Indi Rockin Roll Non Veg customizable: False

id: 138, name:  Zesty Chicken Pocket customizable: False

id: 139, name:  Oreo & Cream (Inclusive of frozen dessert handling charges) customizable: False

id: 140, name:  Choco Sundae (Inclusive of frozen dessert handling charges) customizable: False

id: 141, name:  Cornetto Double Chocolate (Inclusive of frozen dessert handling charges) customizable: False

id: 142, name:  Choco Volcano customizable: False

id: 143, name:  Pepsi Black customizable: False

id: 144, name:  7up Pet Bottle customizable: False

id: 145, name:  Mirinda Pet Bottle customizable: False

id: 146, name:  Pepsi Pet Bottle customizable: False
'''