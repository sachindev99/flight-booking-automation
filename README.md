# Flight Booking — Test Automation

End-to-end test automation project for the **Flight Booking** application

The framework covers **UI automation, API testing, and hybrid API + UI testing** using Python, Playwright, Pytest, and Pytest-BDD.

## Tech Stack

* Python
* Playwright
* Pytest
* Pytest-BDD
* REST API testing
* Page Object Model (POM)
* Git & GitHub

## Testing Approach

This project uses three complementary testing approaches:

### 1. UI Tests

UI tests validate the application through the browser.

Examples:

* Search for flights
* Select departure and return flights
* Enter passenger details
* Validate form errors
* Complete a booking
* Verify booking confirmation

### 2. API Tests

API tests validate backend services directly without going through the browser.

Examples:

* Validate API responses
* Verify status codes
* Validate response data
* Test booking-related endpoints
* Validate error responses

### 3. Hybrid API + UI Tests

Hybrid tests combine API and UI automation to create faster and more realistic end-to-end tests.

For example:

```text
API
 ↓
Create / prepare test data
 ↓
UI
 ↓
Search for flight
 ↓
Select flight
 ↓
Complete booking
 ↓
UI validation
 ↓
API
 ↓
Verify booking data
```

This approach allows API calls to handle test-data setup or backend validation while Playwright handles the user-facing workflow.

## Project Structure

```text
flight-booking-automation/
│
├── features/
│   ├── flight_booking.feature
│   └── api_ui_booking.feature
│
├── pageObjects/
│   └── flight_booking_page.py
│
├── api/
│   ├── api_client.py
│   └── booking_api.py
│
├── steps/
│   ├── test_flight_booking.py
│   └── test_api_ui_booking.py
│
├── utils/
│   └── test_data.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Test Cases

### TC01: One-way Booking — Happy Path

**Steps:**

1. Search for a one-way trip.
2. Select a flight and continue.
3. Enter passenger details.
4. Complete payment and confirm the booking.

**Expected Result:**

A **"Booking Confirmed!"** screen is displayed with a booking reference (PNR).

### TC02: Round-trip Booking

**Steps:**

1. Leave the **One Way** checkbox unticked.
2. Search for flights.
3. Select a departure and return flight.
4. Complete passenger details and payment.

**Expected Result:**

Both flights appear on the confirmation page and the total reflects the combined fares.

### TC03: Return Date — Round Trips Only

**Steps:**

1. Toggle the **One Way** checkbox.

**Expected Result:**

* One Way selected → Return Date is hidden.
* One Way not selected → Return Date is displayed.

### TC04: Search Validation

**Steps:**

1. Leave From and To fields empty.
2. Click **Search Flights**.

**Expected Result:**

Inline validation errors are displayed for the missing required fields.

### TC05: Same Origin and Destination

**Steps:**

1. Select the same city for From and To.
2. Click **Search Flights**.

**Expected Result:**

A validation error is displayed and the search is prevented.

### TC06: Sort Results by Price

**Steps:**

1. Search for flights.
2. Select **Price: Low to High**.

**Expected Result:**

Flights are reordered from the lowest price to the highest price.

### TC07: Filter Non-stop Flights

**Steps:**

1. Search for flights.
2. Select **Non-stop only**.

**Expected Result:**

Only non-stop flights remain in the results.

### TC08: Continue Disabled Until Flight Selection

**Steps:**

1. Search for flights.
2. Do not select a flight.

**Expected Result:**

The **Continue to passenger details** button remains disabled.

### TC09: Passenger Validation

**Steps:**

1. Proceed to passenger details.
2. Enter an invalid email address.
3. Submit the passenger details.

**Expected Result:**

An email validation error is displayed and the user cannot proceed.

### TC10: Total Reflects Number of Passengers

**Steps:**

1. Set the number of passengers to 2.
2. Select the required flight(s).
3. Proceed to payment.

**Expected Result:**

The total equals the selected fare(s) multiplied by the number of passengers.

## Hybrid API + UI Scenarios

Additional hybrid scenarios will be added to demonstrate API and UI integration.

### Hybrid TC01: API Test Data + UI Booking

**Flow:**

1. Use an API to prepare or retrieve required test data.
2. Launch the application through Playwright.
3. Search for a flight using the API-provided data.
4. Select the flight.
5. Complete the booking through the UI.
6. Capture the booking reference.
7. Use the API to validate the created booking.

**Expected Result:**

The booking is successfully created through the UI and the backend API confirms the expected booking data.

### Hybrid TC02: UI Booking + API Validation

**Flow:**

```text
UI → Create Booking
       ↓
Capture PNR
       ↓
API → Retrieve Booking
       ↓
Validate booking details
```

**Expected Result:**

The booking information displayed in the UI matches the booking information returned by the API.

## Test Execution

### Run all tests

```bash
pytest
```

### Run with browser visible

```bash
pytest --headed
```

### Run with print output

```bash
pytest --headed -s
```

### Run a specific feature

```bash
pytest features/flight_booking.feature
```

## Automation Architecture

The framework follows a **Page Object Model** architecture for UI automation and separates API functionality into reusable API clients.

```text
                    Test Scenarios
                          │
              ┌───────────┴───────────┐
              │                       │
             UI                      API
              │                       │
        Playwright              API Client
              │                       │
        Page Objects             Endpoints
              │                       │
              └───────────┬───────────┘
                          │
                    Hybrid Tests
```

This separation keeps the framework maintainable and allows API and UI components to be reused independently.

## Goals of the Project

This project is being developed to demonstrate practical QA automation skills including:

* UI automation
* API testing
* Hybrid API + UI testing
* BDD with Gherkin
* Page Object Model
* Test data management
* Functional validation
* End-to-end testing
* Reusable automation components
* Git/GitHub version control
