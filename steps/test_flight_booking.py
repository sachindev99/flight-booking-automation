import pytest


from pytest_bdd import scenarios, given, when, parsers, then

from pageObjects.booking_confirmation import BookingConfirmation
from pageObjects.flight_booking_page import FlightBookingPage
from pageObjects.passenger_details import PassengerDetails
from pageObjects.payment_details import PaymentDetails

scenarios("../features/flight_booking.feature")


@pytest.fixture
def flight_booking_page(page):
    return FlightBookingPage(page)

@pytest.fixture
def passenger_details_page(page):
    return PassengerDetails(page)

@pytest.fixture
def payment_details_page(page):
    return PaymentDetails(page)

@pytest.fixture
def booking_confirmation_page(page):
    return BookingConfirmation(page)


@given('user is on the flight booking site')
def given_user_flight_booking_site(flight_booking_page):
    flight_booking_page.go_to_flight_booking_site()

@given('user selects the From and To locations')
def given_user_flight_booking_locations(flight_booking_page,datatable):
    from_city,to_city=datatable[0]
    print(from_city,to_city)

    flight_booking_page.select_arrival_and_departure_location(from_city,to_city)


@given('user selects the departure date and number of passengers')
def user_selects_the_departure_date_and_number_of_passengers(flight_booking_page):
    flight_booking_page.select_departure_date_and_number_of_passengers()

@given('user selects the return date')
def user_selects_the_return_date(flight_booking_page):
    flight_booking_page.select_return_date()

@given('user selects the one way trip')
def user_selects_the_one_way_trip(flight_booking_page):
    flight_booking_page.select_one_way_trip()

@given('user selects the travel class')
def user_selects_the_travel_class(flight_booking_page):
    flight_booking_page.select_travel_class()

@given('user clicks the search flight button')
def user_clicks_the_search_flight_button(flight_booking_page):
    flight_booking_page.search_flight_button()

@when(parsers.parse('user selects a "{airline}" departure flight from the list'))
def user_clicks_the_departure_flight_from_list(flight_booking_page,airline):
    flight_booking_page.select_departure_flight_from_list(airline)

@when(parsers.parse('user selects a "{airline}" return flight from the list'))
def user_clicks_the_return_flight_from_list(flight_booking_page,airline):
    flight_booking_page.select_return_flight_from_list(airline)

@when('proceed to the customer details page')
def proceed_to_user_customer_details(flight_booking_page):
    flight_booking_page.click_on_continue_to_passenger_details_button()

@when('user enters passenger details')
def enter_passenger_details(passenger_details_page):
    passenger_details_page.enter_passenger_details()


@when('user enters payment details')
def enter_payment_details(payment_details_page):
    payment_details_page.enter_payment_details()

@then('booking should be confirmed')
def booking_is_confirmed(booking_confirmation_page):
    booking_confirmation_page.get_booking_confirmation()

