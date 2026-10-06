import time

from playwright.sync_api import Page


class PassengerDetails:
    def __init__(self,page:Page):
        self.page=page


    def enter_passenger_details(self):
        self.page.get_by_placeholder("Ada Lovelace").fill("Test User")
        self.page.get_by_placeholder("you@example.com").fill("test@gmail.com")
        self.page.get_by_test_id("flight-passenger-phone").fill("+15556666666")
        self.page.get_by_role("button",name="Continue to payment →").click()
