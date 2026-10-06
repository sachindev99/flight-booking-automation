from playwright.sync_api import Page


class PaymentDetails:
    def __init__(self,page:Page):
        self.page = page


    def enter_payment_details(self):
        self.page.get_by_test_id("flight-card-number").fill("4511 1122 2233 4444")
        self.page.get_by_placeholder("MM/YY").fill("05/26")
        self.page.get_by_test_id("flight-cvv").fill("123")
        self.page.get_by_role("button",name="Pay & Confirm Booking").click()