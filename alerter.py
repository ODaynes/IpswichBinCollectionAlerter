# Script created by Owen Daynes

# selenium imported for web page manipulation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# sleep imported to force script to wait for page update

from time import sleep


if __name__ == "__main__":

    # prompt user for street name

    road_name = str(input("Please enter your street or road name: "))
    not_found_string = 'Your search term: "%s" did not match any street names.' % road_name
    driver = ""

    # attempt to find usable browser

    try:
        driver = webdriver.Firefox("drivers/geckodriver.exe")
    except:
        print("Cannot access Mozilla FireFox.")
        try:
            driver = webdriver.Chrome("drivers/chromedriver.exe")
        except:
            print("Cannot access Google Chrome")
            try:
                driver = webdriver.Edge("drivers/MicrosoftWebDriver.exe")
            except:
                print("Cannot access Microsoft Edge")
                print()
                print("No more browsers to use - terminating script...")
                exit(1)

    # access website

    driver.get("https://app.ipswich.gov.uk/bin-collection/")
    input_field = driver.find_element_by_name("txtStreet")
    input_field.send_keys(road_name + Keys.ENTER)

    # force script to wait for page update

    sleep(0.5)

    content = driver.find_element_by_class_name("ibc-pane")

    result = ""

    if not_found_string in content.text:
        result = "Sorry, \"%s\" could not be found." % road_name
    else:
        unordered_list = content.find_element_by_tag_name("ul")
        responses = unordered_list.find_elements_by_tag_name("li")
        result = responses[0].text

    # write result to console - soon to be updated to alert user by text or e-mail

    print(result)

    # close browser

    driver.close()