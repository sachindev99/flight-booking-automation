import pytest


from pytest_bdd import scenarios, given

from pageObjects.flight_booking_page import FlightBookingPage

scenarios("../features/flight_booking.feature")


@pytest.fixture
def flight_booking_page(page):
    return FlightBookingPage(page)



@given('user is on the flight booking site')
def given_user_flight_booking_site(flight_booking_page):
    flight_booking_page.go_to_flight_booking_site()



