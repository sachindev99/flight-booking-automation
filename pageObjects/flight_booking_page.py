import time
from datetime import date, timedelta

from playwright.sync_api import Page, expect


class FlightBookingPage:
    def __init__(self, page:Page):
        self.current_date = date.today()
        self.page = page
        self.flight_city= page.get_by_test_id("flight-from")
        self.to_city= page.get_by_test_id("flight-to")
        self.departure_date=page.get_by_test_id('flight-departure-date')
        self.num_of_passengers=page.get_by_test_id('flight-passengers')
        self.return_date=page.get_by_test_id('flight-return-date')
        self.one_way=page.get_by_label('One Way')
        self.flight_class=page.get_by_test_id('flight-class')
        self.search_flight_btn= page.get_by_role("button", name="Search Flights")
        self.continue_to_passenger_details_btn=page.get_by_role("button", name="Continue to passenger details →")

    def go_to_flight_booking_site(self):
        self.page.goto('https://www.qapractice.com/flight-booking-scenarios')


    def select_arrival_and_departure_location(self,from_city,to_city):
        self.flight_city.select_option(from_city)
        self.to_city.select_option(to_city)

    def select_departure_date_and_number_of_passengers(self):
        departure_day= self.current_date.strftime("%Y-%m-%d")
        self.departure_date.fill(departure_day)
        self.num_of_passengers.fill('2')

    def select_return_date(self):
        return_date = self.current_date+timedelta(days=7)
        return_date=return_date.strftime("%Y-%m-%d")
        self.return_date.fill(return_date)

    def select_one_way_trip(self):
        self.one_way.check()

    def select_travel_class(self):
        self.flight_class.select_option('First')

    def search_flight_button(self):
        self.search_flight_btn.click()

    def select_departure_flight_from_list(self,airline):
        flight= self.page.get_by_test_id(f'flight-result-{airline}')
        flight.get_by_role('button',name="Select").click()


    def click_on_continue_to_passenger_details_button(self):
        self.continue_to_passenger_details_btn.click()

    def select_return_flight_from_list(self, airline):
        flight = self.page.get_by_test_id(f'flight-result-{airline}')
        flight.get_by_role('button', name="Select").click()

    def return_date_is_not_visible(self):
        expect(self.return_date).not_to_be_visible()

    def unticked_one_way_trip(self):
        self.one_way.uncheck()

    def return_date_is_visible(self):
        expect(self.return_date).to_be_visible()

    def from_field_validation(self):
        expect(self.page.get_by_text('Please select a departure city.')).to_be_visible()

    def to_field_validation(self):
        expect(self.page.get_by_text('Please select a destination city.')).to_be_visible()

    def validation_error_for_identical_cities(self):
        expect(self.page.get_by_text('Departure and destination cities cannot be the same.')).to_be_visible()








