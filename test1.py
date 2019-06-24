from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

import globals as gbl

def test1(populate_globals):
    driver = populate_globals
    # driver = webdriver.Chrome("chromedriver.exe")
    # driver.implicitly_wait(10000)  # seconds
    # driver.maximize_window()
    # driver.get("https://rozetka.com.ua/ua/")
    driver.find_element_by_css_selector('.exponea-close-cross').click()
    driver.find_element_by_css_selector('.header-topline__user-link.link-dashed').click()
    driver.find_element_by_css_selector("#auth_email").click()
    driver.find_element_by_css_selector("#auth_email").send_keys(gbl.my_data['username'])
    driver.find_element_by_css_selector("#auth_pass").click()
    driver.find_element_by_css_selector("#auth_pass").send_keys(gbl.my_data['password'])
    driver.find_element_by_css_selector("button.button_color_navy.auth-modal__login-button").click()
    gbl.my_data['username']="sff"
    print(gbl.my_data)

def test13333():
    print(gbl.my_data)
    # action_chains = ActionChains(driver)
    # element = driver.find_element_by_partial_link_text("Краса та здоров’я")
    # action_chains.move_to_element(element).perform()
    # driver.find_element_by_partial_link_text("Фотоепілятори").click()
    # driver.find_element_by_css_selector('#rz-banner-img+.exponea-close .exponea-close-cross').click()
    # driver.find_element_by_css_selector('.sort-view-link').click()
    # driver.find_element_by_css_selector('#filter_sortcheap').click()
    # a = driver.find_elements_by_xpath('//a[contains(text(), "IPL6780")]')[0].click()
    # # a = driver.find_elements_by_xpath('//a[contains(text(), "Фотоепілятор BABYLISS G935E")]')
    # # a[0].click()
    # assert driver.find_element_by_css_selector('.detail-buy-btn-wrap button').is_enabled(), "Button is not active"
    # # action_chains.move_to_element(driver.find_element_by_partial_link_text('IPL6780')).perform()
    # # driver.find_element_by_css_selector('.g-buy-submit-link').click()
    #
    # sleep(5)
