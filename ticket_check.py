#!/usr/bin/env python3

import time
import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException

def check_ticket(url):
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    while driver.page_source.find("Know Before You Arrive") == -1:
        time.sleep(1)
    # Wait for the API call to finish.
    time.sleep(2)
    found = False
    try:
        driver.find_element_by_class_name("liftTicketsResults__book_by");
        found = True
        print("found")
    except NoSuchElementException:
        print("not found")
    driver.close()
    return found


if __name__ == "__main__":
    url_good = "https://www.stevenspass.com/plan-your-trip/lift-access/tickets.aspx?startDate=03%2F10%2F2021&numberOfDays=1&ageGroup=Adult"
    url_bad = "https://www.stevenspass.com/plan-your-trip/lift-access/tickets.aspx?startDate=03%2F07%2F2021&numberOfDays=1&ageGroup=Adult"
    print("Checking 3/10")
    check_ticket(url_good)
    print("Checking 3/7")
    check_ticket(url_bad)
