import sys
import time

sys.path.append('..')

from SwiggyCrawler import SwiggyCrawler

crawler = SwiggyCrawler()
time.sleep(10)
# GPT reads the objective and searches Pizza
# Action search["Pizza", "Restaurant"]
crawler.search_suggest("Pizza")
found = crawler.search("Pizza", "Restaurant")
if not found:
    exit()

print("Search Results")
output = crawler.render_search_restaurants()
print(output)
# GPT reads the search results and chooses the restaurant at index 2
# Action click[2]
crawler.search_restaurant_by_index(2)

print("Menu Items")
output = crawler.render_menu_items()
print(output)
# GPT looks at the menu items and chooses to order two index 157
# Action add[157, 2]
crawler.add_menu_item_by_index_x_times(157, 2)

# Action checkout
crawler.checkout()
time.sleep(20)
'''
Search Results

id: 0, name:  Domino's Pizza,  status: Open

id: 1, name:  Crusto's - Cheese Burst Pizza,  status: Open

id: 2, name:  La Pino'z Pizza,  status: Open

id: 3, name:  Pizza Hut,  status: Open

id: 4, name:  Raffaele's Ristorante Pizzeria,  status: Open

id: 5, name:  Yumlane Pizza,  status: Open

id: 6, name:  Fiero! Pizzeria,  status: Open

id: 7, name:  Piazza pizza by Little Italy,  status: Open

id: 8, name:  Olio - The Wood Fired Pizzeria,  status: Open

id: 9, name:  Onesta,  status: Open

id: 10, name:  US Pizza,  status: Open

id: 11, name:  Pepe's Pizza,  status: Open

id: 12, name:  Say Cheese! Pizza,  status: Open

id: 13, name:  Pizza Queen Lover,  status: Open

id: 14, name:  THE PIZZA QUEEN,  status: Open

id: 15, name:  Pizza Party,  status: Open

id: 16, name:  Fresh crunch pizza,  status: Open

id: 17, name:  Tottos pizza,  status: Open

id: 18, name:  Joey's Pizza Express Delivery,  status: Open

id: 19, name:  GOPIZZA,  status: Open

id: 20, name:  The Lio' Pizza,  status: Open

id: 21, name:  Crazy Pizza,  status: Open

id: 22, name:  Deshi Fusion Pizza,  status: Open

id: 23, name:  Pizza Kingdom,  status: Open

id: 24, name:  Ciro's Pizzeria,  status: Open

id: 25, name:  5th Avenue Cafe,  status: Open

id: 26, name:  The Bier Library,  status: Open

id: 27, name:  ELITE DELICACY,  status: Open

id: 28, name:  46 Ounces,  status: Open

id: 29, name:  Lets Talk Over Table Cafe,  status: Open

id: 30, name:  Cafe Hideout,  status: Open

id: 31, name:  Friends Euro Restaurant ,  status: Open

id: 32, name:  1522 The Pub - Residency Road,  status: Open

id: 33, name:  Cafetainment,  status: Open

id: 34, name:  Biergarten Brewery & Kitchen,  status: Open

id: 35, name:  Watson's,  status: Open

id: 36, name:  Tipsy Bull The Bar Exchange,  status: Open

id: 37, name:  Shiv Sagar ( RS ),  status: Open

id: 38, name:  1131 BAR+KITCHEN,  status: Open

id: 39, name:  Cafe Amor ,  status: Open

id: 40, name:  PIZZAAJ,  status: Open

id: 41, name:  Appu's pizzeria,  status: Open

id: 42, name:  Cafezza,  status: Open

id: 43, name:  Chinese Connection,  status: Open

id: 44, name:  China Social,  status: Open

id: 45, name:  Happy Orange,  status: Open

id: 46, name:  KRUST,  status: Open

id: 47, name:  De Zyka Cafe,  status: Open

id: 48, name:  EatFit Pizzeria,  status: Open

id: 49, name:  Qube Cafe,  status: Open

id: 50, name:  limelight-Royal Orchid Hotel,  status: Open

id: 51, name:  Ovenfresh Cakes And Desserts,  status: Open

id: 52, name:  TBK Rolls & Grills,  status: Open

id: 53, name:  Buono!,  status: Open

id: 54, name:  Nanav Stores and Cafe,  status: Open

id: 55, name:  The California Bar & Kitchen     ,  status: Open

id: 56, name:  Burger to Rice Bowl Co. (BRB),  status: Open

id: 57, name:  NAMMA ADDA,  status: Open

id: 58, name:  The Living Room,  status: Open

Menu Items for La Pino's Pizza

id: 0, name:  Margherita Pizza (personal Giant Slice (22, customizable: True, available: 
True

id: 1, name:  Makhani Do Pyaza (personal Giant Slice (22, customizable: True, available: 
True

id: 2, name:  My Mac (personal Giant Slice (22, customizable: True, available: True      

id: 3, name:  Onion Blossom (personal Giant Slice (22, customizable: True, available: True

id: 4, name:  Sweet Corns Delight (personal Giant Slice (22, customizable: True, available: True

id: 5, name:  Country Side Pizza (personal Giant Slice (22, customizable: True, available: True

id: 6, name:  Garden Delight Pizza (personal Giant Slice (22, customizable: True, available: True

id: 7, name:  Lovers Bite Pizza (personal Giant Slice (22, customizable: True, available: True

id: 8, name:  Spring Fling Pizza (personal Giant Slice (22, customizable: True, available: True

id: 9, name:  Burn To Hell Pizza (personal Giant Slice (22, customizable: True, available: True

id: 10, name:  Cheezy-7 Pizza (personal Giant Slice (22, customizable: True, available: True

id: 11, name:  Farm Villa Pizza (personal Giant Slice (22, customizable: True, available: True

id: 12, name:  Garden Special Pizza (personal Giant Slice (22, customizable: True, available: True

id: 13, name:  Macaroni Special Pizza (personal Giant Slice (22, customizable: True, available: True

id: 14, name:  Paneer Tikka Butter Masala Pizza (personal Giant Slice (22, customizable: 
True, available: True

id: 15, name:  Veg, customizable: True, available: True

id: 16, name:  Veg Tamer Pizza (personal Giant Slice (22, customizable: True, available: 
True

id: 17, name:  African Peri Peri Veg Pizza (personal Giant Slice (22, customizable: True, available: True

id: 18, name:  Cheese Lover Pizza (personal Giant Slice (22, customizable: True, available: True

id: 19, name:  Cheesy Macaroni Veg Pizza (personal Giant Slice (22, customizable: True, available: True

id: 20, name:  English Retreat Pizza (personal Giant Slice (22, customizable: True, available: True

id: 21, name:  Garlic-to-pizza (personal Giant Slice (22, customizable: True, available: 
True

id: 22, name:  Hot Passion Pizza (personal Giant Slice (22, customizable: True, available: True

id: 23, name:  Korma Special Pizza (personal Giant Slice (22, customizable: True, available: True

id: 24, name:  La Pino'z Paneer Pizza (personal Giant Slice (22, customizable: True, available: True

id: 25, name:  Las Vegas Treat Pizza (personal Giant Slice (22, customizable: True, available: True

id: 26, name:  Peri Peri Veg Pizza (personal Giant Slice (22, customizable: True, available: True

id: 27, name:  Super BBQ (personal Giant Slice (22, customizable: True, available: True  

id: 28, name:  Exotic Tikka Pizza (personal Giant Slice (22, customizable: True, available: True

id: 29, name:  Hawaiian Special (personal Giant Slice (22, customizable: True, available: True

id: 30, name:  Korma Delight (personal Giant Slice (22, customizable: True, available: True

id: 31, name:  Seekh Special (personal Giant Slice (22, customizable: True, available: True

id: 32, name:  Chicago Delight Pizza (personal Giant Slice (22, customizable: True, available: True

id: 33, name:  Chicken De-light Pizza (personal Giant Slice (22, customizable: True, available: True

id: 34, name:  Tandoori Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 35, name:  Texas Bbq'ed Pizza (personal Giant Slice (22, customizable: True, available: True

id: 36, name:  Hot Tandoori Pizza (personal Giant Slice (22, customizable: True, available: True

id: 37, name:  Indian Chicken Special Pizza (personal Giant Slice (22, customizable: True, available: True

id: 38, name:  Korma Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 39, name:  La Pino'z Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 40, name:  Mixed Grill Pizza (personal Giant Slice (22, customizable: True, available: True

id: 41, name:  Non-veg Hawaiian Pizza (personal Giant Slice (22, customizable: True, available: True

id: 42, name:  Non-veg Tamer Pizza (personal Giant Slice (22, customizable: True, available: True

id: 43, name:  California Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 44, name:  Cheesy Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 45, name:  Cheesy Macaroni Non-veg Pizza (personal Giant Slice (22, customizable: True, available: True

id: 46, name:  Chicken Tikka Lababdar Pizza (personal Giant Slice (22, customizable: True, available: True

id: 47, name:  Fire-e-chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 48, name:  Meat Blast Pizza (personal Giant Slice (22, customizable: True, available: True

id: 49, name:  Peri Peri - Chicken Pizza (personal Giant Slice (22, customizable: True, available: True

id: 50, name:  Spanish Sizzles Pizza (personal Giant Slice (22, customizable: True, available: True

id: 51, name:  2 Medium Pizza Starting At Rs 649, customizable: True, available: True    

id: 52, name:  2 Medium Non-veg Pizza @ 649, customizable: True, available: True

id: 53, name:  Pesto Veg, customizable: False, available: True

id: 54, name:  Spicy Veg, customizable: False, available: True

id: 55, name:  Cheesy, customizable: False, available: True

id: 56, name:  Korma Pyaza, customizable: False, available: True

id: 57, name:  Loaded Pesto, customizable: False, available: True

id: 58, name:  Tomatoes Pizza, customizable: False, available: False

id: 59, name:  Onions Pizza, customizable: False, available: False

id: 60, name:  Capsicum Pizza, customizable: False, available: False

id: 61, name:  Sweet Corns Pizza, customizable: False, available: False

id: 62, name:  Onions & Capsicum Pizza, customizable: False, available: False

id: 63, name:  Capsicum & Paneer Pizza, customizable: False, available: False

id: 64, name:  Jalapenos & Olives Pizza, customizable: False, available: False

id: 65, name:  Onions & Paneer Pizza, customizable: False, available: False

id: 66, name:  Capsicum, Paneer & Red Paprika Pizza, customizable: False, available: False

id: 67, name:  Jalapenos, Sweet Corns & Paneer Pizza, customizable: False, available: False

id: 68, name:  Pesto Non-veg, customizable: False, available: True

id: 69, name:  Spicy Non-veg, customizable: False, available: True

id: 70, name:  Korma Non-veg, customizable: False, available: True

id: 71, name:  Bbq Chicken Pizza, customizable: False, available: False

id: 72, name:  Capsicum & Chicken Tikka Pizza, customizable: False, available: False     

id: 73, name:  Chicken Seekh & Chicken Salami Pizza, customizable: False, available: False

id: 74, name:  Chicken Tikka & Chicken Salami Pizza, customizable: False, available: False

id: 75, name:  Keema & Onion Pizza, customizable: False, available: False

id: 76, name:  Margherita Pizza, customizable: True, available: True

id: 77, name:  Makhani Do Pyaza, customizable: True, available: True

id: 78, name:  My Mac, customizable: True, available: True

id: 79, name:  Onion Blossoms, customizable: True, available: True

id: 80, name:  Sweet Corns Delight, customizable: True, available: True

id: 81, name:  Country Side Pizza, customizable: True, available: True

id: 82, name:  Garden Delight Pizza, customizable: True, available: True

id: 83, name:  Lovers Bite Pizza, customizable: True, available: True

id: 84, name:  Spring Fling Pizza, customizable: True, available: True

id: 85, name:  Cheezy-7 Pizza, customizable: True, available: True

id: 86, name:  Burn To Hell Pizza, customizable: True, available: True

id: 87, name:  Farm Villa Pizza, customizable: True, available: True

id: 88, name:  Garden Special Pizza, customizable: True, available: True

id: 89, name:  Macaroni Special Pizza, customizable: True, available: True

id: 90, name:  Paneer Tikka Butter Masala Pizza, customizable: True, available: True     

id: 91, name:  Veg, customizable: True, available: True

id: 92, name:  Cheese Lover Pizza, customizable: True, available: True

id: 93, name:  Garlic-to-pizza, customizable: True, available: True

id: 94, name:  African Peri Peri Veg Pizza, customizable: True, available: True

id: 95, name:  Cheesy Macaroni Veg Pizza, customizable: True, available: True

id: 96, name:  English Retreat Pizza, customizable: True, available: True

id: 97, name:  Hot Passion Pizza, customizable: True, available: True

id: 98, name:  Korma Special Pizza, customizable: True, available: True

id: 99, name:  La Pino'z Paneer Pizza, customizable: True, available: True

id: 100, name:  Las Vegas Treat Pizza, customizable: True, available: True

id: 101, name:  Peri Peri Veg Pizza, customizable: True, available: True

id: 102, name:  Veg Tamer Pizza, customizable: True, available: True

id: 103, name:  Super BBQ, customizable: True, available: True

id: 104, name:  Exotic Tikka Pizza, customizable: True, available: True

id: 105, name:  Hawaiian Special, customizable: True, available: True

id: 106, name:  Korma Delight, customizable: True, available: True

id: 107, name:  Seekh Special, customizable: True, available: True

id: 108, name:  Tandoori Chicken Pizza, customizable: True, available: True

id: 109, name:  Chicago Delight Pizza, customizable: True, available: True

id: 110, name:  Chicken De-light Pizza, customizable: True, available: True

id: 111, name:  Texas Bbq'ed Pizza, customizable: True, available: True

id: 112, name:  Hot Tandoori Pizza, customizable: True, available: True

id: 113, name:  Indian Chicken Special Pizza, customizable: True, available: True        

id: 114, name:  Korma Chicken Pizza, customizable: True, available: True

id: 115, name:  La Pino'z Chicken Pizza, customizable: True, available: True

id: 116, name:  Mixed Grill Pizza, customizable: True, available: True

id: 117, name:  Non-veg Hawaiian Pizza, customizable: True, available: True

id: 118, name:  California Chicken Pizza, customizable: True, available: True

id: 119, name:  Cheesy Chicken Pizza, customizable: True, available: True

id: 120, name:  Peri Peri - Chicken Pizza, customizable: True, available: True

id: 121, name:  Cheesy Macaroni Non-veg Pizza, customizable: True, available: True       

id: 122, name:  Chicken Tikka Lababdar Pizza, customizable: True, available: True        

id: 123, name:  Fire-e-chicken Pizza, customizable: True, available: True

id: 124, name:  Meat Blast Pizza, customizable: True, available: True

id: 125, name:  Spanish Sizzles Pizza, customizable: True, available: True

id: 126, name:  Non-veg Tamer Pizza, customizable: True, available: True

id: 127, name:  Classic Pizzas Pack Of 4 - Veg, customizable: False, available: True     

id: 128, name:  Classic Pizzas Pack Of 4 - Veg, customizable: False, available: True     

id: 129, name:  Classic Pizzas Pack Of 4 - Non-veg, customizable: False, available: True 

id: 130, name:  Plain Garlic Bread, customizable: True, available: True

id: 131, name:  Cheesy Garlic Bread, customizable: True, available: True

id: 132, name:  Supreme Garlic Bread, customizable: True, available: True

id: 133, name:  Paneer Tikka Garlic Bread, customizable: True, available: True

id: 134, name:  English Chicken Garlic Bread, customizable: True, available: True        

id: 135, name:  Chicken Tikka Garlic Bread, customizable: True, available: True

id: 136, name:  Mutton Keema Garlic Bread, customizable: True, available: True

id: 137, name:  Garlic Bread Sticks, customizable: True, available: True

id: 138, name:  Sweet Corn Stuffed Garlic Bread, customizable: True, available: True     

id: 139, name:  Paneer Tikka Stuffed Garlic Bread, customizable: True, available: True   

id: 140, name:  Mutton Keema Stuffed Garlic Bread, customizable: True, available: True   

id: 141, name:  Veg Lasagna - Creamy White, customizable: False, available: True

id: 142, name:  Veg Lasagna - Pesto, customizable: False, available: True

id: 143, name:  Veg Lasagna - Rosy Red, customizable: False, available: True

id: 144, name:  Non Veg Lasagna - Creamy White, customizable: False, available: True     

id: 145, name:  Non Veg Lasagna - Pesto, customizable: False, available: True

id: 146, name:  Non Veg Lasagna - Rosy Red, customizable: False, available: True

id: 147, name:  Veg Spaghetti - Creamy White, customizable: False, available: True       

id: 148, name:  Veg Spaghetti - Pesto, customizable: False, available: True

id: 149, name:  Veg Spaghetti - Rosy Red, customizable: False, available: True

id: 150, name:  Spaghetti With Meat Balls - Creamy White, customizable: False, available: True

id: 151, name:  Spaghetti With Meat Balls - Pesto, customizable: False, available: True  

id: 152, name:  Spaghetti With Meat Balls - Rosy Red, customizable: False, available: True

id: 153, name:  Mexicana Pasta Veg, customizable: False, available: True

id: 154, name:  Americano Pasta Veg, customizable: False, available: True

id: 155, name:  Indiana Pasta Veg, customizable: False, available: True

id: 156, name:  Italiano Pasta Veg, customizable: False, available: True

id: 157, name:  Mexicana Pasta Non-veg, customizable: False, available: True

id: 158, name:  Americano Pasta Non-veg, customizable: False, available: True

id: 159, name:  Indiana Pasta Non-veg, customizable: False, available: True

id: 160, name:  Italiano Pasta Non-veg, customizable: False, available: True

id: 161, name:  Mushrooms, Corns & Onion Taco's, customizable: False, available: True    

id: 162, name:  Paneer & Corns Taco's, customizable: False, available: True

id: 163, name:  Paneer Tikka Butter Masala & Red Paprika Taco's, customizable: False, available: True

id: 164, name:  Chicken Seekh Kebab & Chicken Bbq Taco's, customizable: False, available: True

id: 165, name:  Chicken Tikka & Chicken Salami Taco's, customizable: False, available: True

id: 166, name:  Macaroni & Cheese Veg, customizable: False, available: True

id: 167, name:  Smoke Chilli Macaroni Veg, customizable: False, available: True

id: 168, name:  Macaroni & Cheese Non-veg, customizable: False, available: True

id: 169, name:  Smoke Chilli Macaroni Non-veg, customizable: False, available: True      

id: 170, name:  Hot & Spicy Wings, customizable: True, available: True

id: 171, name:  Mutton Shammi Kabab, customizable: True, available: True

id: 172, name:  Peri Peri Wings, customizable: True, available: True

id: 173, name:  Chicken Meatballs, customizable: True, available: True

id: 174, name:  Paneer, Sweet Corn & Cheese Quesadillas, customizable: False, available: 
False

id: 175, name:  Mushroom, Olives & Cheese Quesadillas, customizable: False, available: False

id: 176, name:  Bbq Chicken & Cheese Quesadillas, customizable: False, available: False  

id: 177, name:  Chicken Tikka, Jalapenos & Cheese Quesadillas, customizable: False, available: False

id: 178, name:  Red Velvet Lava Cake, customizable: False, available: True

id: 179, name:  Choco Lava, customizable: False, available: True

id: 180, name:  Cheese Dip, customizable: False, available: True

id: 181, name:  Jalapeno Dip, customizable: False, available: True

id: 182, name:  Peri Peri Dip, customizable: False, available: True

id: 183, name:  Garlic & Herb Dip, customizable: False, available: True

id: 184, name:  Mustard Dip, customizable: False, available: True

id: 185, name:  Quesadilla Pack Of 4 (veg), customizable: False, available: False        

id: 186, name:  Quesadilla Pack Of 4 (non - Veg), customizable: False, available: False  
'''