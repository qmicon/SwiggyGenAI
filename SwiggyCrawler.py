from playwright.sync_api import Playwright, sync_playwright
import time

class SwiggyCrawler:
    def __init__(self):
        self.browser = (
			sync_playwright()
			.start()
			.chromium.launch(
				headless=False,
			)
		)
        self.page = self.browser.new_page()
        self.page.set_default_navigation_timeout(40000)
        self.page.set_default_timeout(40000)
        self.page.goto('https://www.swiggy.com/')
        login_link = self.page.wait_for_selector('a:has-text("Login")')
        login_link.click()
        mobile_input = self.page.wait_for_selector('#mobile')
        print("Type your Mobile Number")
        mobile_number = str(input())
        mobile_input.type(mobile_number)
        form = self.page.wait_for_selector('form')
        login_link = form.wait_for_selector('a:has-text("Login")')
        login_link.click()
        otp_input = self.page.wait_for_selector('#otp')
        print("Type your OTP Number")
        otp_num = str(input())
        otp_input.type(otp_num)
        form = self.page.wait_for_selector('form')
        verify_otp = form.wait_for_selector('a:has-text("VERIFY OTP")')
        verify_otp.click()
        self.page.goto('https://www.swiggy.com/city/bangalore')
        self.page.goto('https://www.swiggy.com/search')
        self.search_suggest_elements = None

    def search_suggest(self, value):
        input_value = self.page.wait_for_selector('input[placeholder="Search for restaurants and food"]')
        input_value.type(value)
        self.page.wait_for_selector('button[data-testid="autosuggest-item"]')
        self.search_suggest_elements = self.page.query_selector_all('button[data-testid="autosuggest-item"]')

    def search(self, value, category="Dish"):
        # Need to call search_suggest first
        if not self.search_suggest_elements:
            print("call search suggest first")
            return

        for button in self.search_suggest_elements:
            res_name, res_category  = self.parse_search_suggest(button)
            if value in res_name and category == res_category:
                button.click()
                if category == 'Restaurant':
                    self.page.wait_for_selector('div[data-testid="search-pl-restaurant-card"]')
                    self.search_elements = self.page.query_selector_all('div[data-testid="search-pl-restaurant-card"]')
                elif category == 'Dish':
                    pass
                return True

        return False

    def search_suggestion_by_index(self, index):
         # Need to call search_suggest first
        if not self.search_suggest_elements:
            print("call search suggest first")
            return

        button = self.search_suggest_elements[index]
        res_name, res_category  = self.parse_search_suggest(button)
        button.click()
        if res_category == 'Restaurant':
            self.page.wait_for_selector('div[data-testid="search-pl-restaurant-card"]')
            self.search_elements = self.page.query_selector_all('div[data-testid="search-pl-restaurant-card"]')
        elif res_category == 'Dish':
            pass

        return res_category


    def parse_search_suggest(self, search_suggest_button):
        elements = search_suggest_button.query_selector_all('div div')
        name, category = None, None
        name = elements[0].inner_text()
        category = elements[1].inner_text()
        return (name, category)

    def render_search_suggestions(self):
        return_string = ""
        for index, button in enumerate(self.search_suggest_elements):
            res_name, res_category  = self.parse_search_suggest(button)
            return_string+= f"\nid: {index}, name: {res_name}, category: {res_category}\n"
        return return_string
    def parse_search_restaurant(self, search_div):
        res = {}
        a_tag = search_div.query_selector('div a')
        text = a_tag.get_attribute('aria-label')
        value = a_tag.get_attribute('data-testid')
        if value == 'closed-resturant-wrapper':
            res["Restaurant Status"] = "Closed"
        elif value == 'resturant-card-anchor-container':
            res["Restaurant Status"] = "Open"
        lines = text.split("\n")
        for line in lines:
            values = line.split(":")
            if len(values) == 2:
                res[values[0]] = values[1]

        return res

    def filter_by_restaurant(self, rating, time):
        for element in self.search_elements:
            rating_f, time_f = False, False
            parsed_res = self.parse_search_restaurant(element)
            if parsed_res["Restaurant Status"] == "Closed":
                continue
            for key in parsed_res.keys():
                if 'Rating' in key:
                    if rating <= float(parsed_res[key].split(",")[0]):
                        rating_f = True
                if 'Delivers' in key:
                    if time >= int(parsed_res[key].split("MINS,")[0]):
                        time_f = True

            if rating_f and time_f:
                element.click()
                self.page.wait_for_selector('div[data-testid="normal-dish-item"]')
                self.menu_elements = self.page.query_selector_all('div[data-testid="normal-dish-item"]')
                self.expand_all_menu_items()
                return

    def render_search_restaurants(self):
        res_string = ""
        for index, element in enumerate(self.search_elements):
            parsed_res = self.parse_search_restaurant(element)
            status = parsed_res["Restaurant Status"]
            name = parsed_res["Restaurant name"]
            res_string+= f"\nid: {index}, name: {name} status: {status}\n"

        return res_string

    def search_restaurant_by_index(self, index):
        try:
            element = self.search_elements[index]
            element.click()
            self.page.wait_for_selector('div[data-testid="normal-dish-item"]')
            self.menu_elements = self.page.query_selector_all('div[data-testid="normal-dish-item"]')
            self.expand_all_menu_items()
        except Exception as e:
            raise Exception(f"cannot find the index: {index}, error: {e}")

    def parse_menu_element(self, menu_div):
        '''
        Non-veg item. 8" Small Five Starch. Costs: 260 rupees, Description: Chicken 65, jalapeno, olives, fresh mozzarella. This item is customizable. Swipe right to add item to cart.

        8" Small Five Starch
        260
        Chicken 65, jalapeno, olives, fresh mozzarella.
        ADD
        +
        Customisable
        
        '''
        return menu_div.inner_text()

    def render_menu_items(self):
        res_string = ""
        for index, element in enumerate(self.menu_elements):
            text = self.parse_menu_element(element)
            IsCustomizable = 'Customisable' in text
            IsNotAvailable = 'Next available' in text
            name = text.split(".")[1]
            res_string+= f"\nid: {index}, name: {name}, customizable: {IsCustomizable}, available: {not IsNotAvailable}\n"

        return res_string

    def expand_all_menu_items(self):
        self.page.wait_for_selector('button[aria-expanded="false"]')
        buttons = self.page.query_selector_all('button[aria-expanded="false"]')
        for button in buttons:
            button.click()

    def add_menu_element(self, menu_div):
        add_button = menu_div.query_selector('div[class^="styles_itemAddButton"]')
        add_button = add_button.query_selector('div')
        add_button.hover()
        add_button.click()

    def add_menu_item(self, name):
        for element in self.menu_elements:
            text = self.parse_menu_element(element)
            if 'Next available' in text:
                print("This item is not available")
                return
            if name in text:
                self.add_menu_element(element)
                if 'Customisable' in text:
                    print("Customization items are not supported, add it manually, you have 10 seconds")
                    time.sleep(10)
                return

    def add_menu_item_by_index(self, index):
        try:
            element = self.menu_elements[index]
            text = self.parse_menu_element(element)
            if 'Next available' in text:
                print("This item is not available")
                return
            self.add_menu_element(element)
            if 'Customisable' in text:
                print("Customization items are not supported, add it manually, you have 10 seconds")
                time.sleep(10)
            return True
        except Exception as e:
            raise Exception(f"cannot find the index: {index}, error: {e}")

    def add_menu_item_by_index_x_times(self, index, x):
        try:
            self.add_menu_item_by_index(index)
            div = self.page.locator('div[class^="styles_itemAddButton"]').nth(index)
            add = div.locator('div div:has-text("+")')
            for _ in range(x-1):
                add.click()
        except Exception as e:
            raise Exception(f"cannot add menu item {index} {x} times, error: {e}")

    def checkout(self):
        try:
            view_cart = self.page.wait_for_selector('#view-cart-btn')
            view_cart.click()
        except Exception as e:
            raise Exception(f"cannot checkout, error: {e}")

    def add_and_checkout_menu_items(self, names):
        for name in names:
            self.add_menu_item(name)

        self.checkout()

    def add_and_checkout_menu_items_by_index(self, index_list):
        for index in index_list:
            self.add_menu_item_by_index(index)

        self.checkout()
        