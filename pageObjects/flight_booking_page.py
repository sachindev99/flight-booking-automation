import time
from datetime import date, timedelta

from playwright.sync_api import Page


class FlightBookingPage:
    def __init__(self, page:Page):
        self.current_date = date.today()
        self.page = page



    def go_to_flight_booking_site(self):
        self.page.goto('https://www.qapractice.com/flight-booking-scenarios')


    def select_arrival_and_departure_location(self,from_city,to_city):
        self.page.get_by_test_id("flight-from").select_option(from_city)
        self.page.get_by_test_id("flight-to").select_option(to_city)

    def select_departure_date_and_number_of_passengers(self):
        departure_date= self.current_date.strftime("%Y-%m-%d")
        self.page.get_by_test_id('flight-departure-date').fill(departure_date)
        self.page.locator("#flight-passengers").fill('2')

    def select_return_date(self):
        return_date = self.current_date+timedelta(days=7)
        return_date=return_date.strftime("%Y-%m-%d")
        self.page.get_by_test_id('flight-return-date').fill(return_date)

    def select_one_way_trip(self):
        self.page.get_by_label('One Way').check()

    def select_travel_class(self):
        self.page.get_by_test_id('flight-class').select_option('First')

    def search_flight_button(self):
        self.page.get_by_role("button",name="Search Flights").click()

    def select_departure_flight_from_list(self,airline):
        flight= self.page.get_by_test_id(f'flight-result-{airline}')
        flight.get_by_role('button',name="Select").click()


    def click_on_continue_to_passenger_details_button(self):
        self.page.get_by_role("button", name="Continue to passenger details →").click()

    def select_return_flight_from_list(self, airline):
        flight = self.page.get_by_test_id(f'flight-result-{airline}')
        flight.get_by_role('button', name="Select").click()









