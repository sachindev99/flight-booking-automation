from playwright.sync_api import Page, expect


class BookingConfirmation:
    def __init__(self,page:Page):
        self.page = page


    def get_booking_confirmation(self):
        expect(self.page.get_by_test_id("flight-booking-success")).to_have_text("Booking Confirmed!")
