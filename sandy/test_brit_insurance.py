import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestBritInsuranceSearch:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_search_ifrs17(self, setup):
        driver = setup
        
        # Step 1: Go to https://www.britinsurance.com/
        driver.get("https://www.britinsurance.com/")

        try:
            allow_button = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
            allow_button.click()
            print("Cookie notification accepted.")
        except Exception as e:
            print("Cookie notification not found or already accepted:", e)
                
        # Step 2: Search for the term “IFRS 17” in the search bar top right
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'component--header__search').click()
        search_bar = driver.find_element(By.NAME, 'k')  
        search_bar.send_keys("IFRS 17")

        # Step 3: Wait for search results to load
        time.sleep(5)  

        # Step 4: Assert that 5 titles are returned from the search
        search_results = driver.find_element(By.CLASS_NAME, 'header--search__results').text.split("\n")
        assert len(search_results) == 5, f"Expected 5 search results, but got {len(search_results)}"

        for result in search_results:
            print(result)

        print("Test passed. 'IFRS 17' search returned the expected results.")

