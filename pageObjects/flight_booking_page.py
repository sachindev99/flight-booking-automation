

class FlightBookingPage:
    def __init__(self, page):
        self.page = page



    def go_to_flight_booking_site(self):
        self.page.goto('https://www.qapractice.com/flight-booking-scenarios')

