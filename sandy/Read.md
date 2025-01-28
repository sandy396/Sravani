# Automated Test for BritInsurance Search

This repository contains an automated Selenium test for the BritInsurance website, specifically focusing on verifying the search functionality for the term “IFRS 17”.

## Prerequisites

Before running the tests, ensure the following:

1. **Python** is installed on your system.
2. **Selenium** WebDriver is installed for your browser.
3. **ChromeDriver** (or any other WebDriver corresponding to your browser) is installed and accessible via your system’s PATH.

### Install dependencies


Test Setup
1. Clone the Repository
Start by cloning the repository to your local machine:


git clone https://github.com/your-username/britinsurance-search-test.git
cd britinsurance-search-test
2. Install dependencies
Install the necessary Python packages using pip:

pip install selenium pytest

To execute the test, run the following command in your terminal:
pytest test_britinsurance.py

###########################

# API Testing for PATCH 'objects/{id}' Endpoint

This repository contains automated tests for the PATCH 'objects/{id}' endpoint of the RESTful API at [https://api.restful-api.dev](https://api.restful-api.dev). The tests include scenarios for updating an existing object and handling non-existent object updates.

## Prerequisites

To run the tests, you need to have the following installed:

- Python 3.8+
- 'pytest' testing framework
- 'requests' library

You can install the dependencies using 'pip':


pip install pytest requests
To execute the test, run the following command in your terminal:
pytest test_patch_requests.py
