from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from random import randint


def test_libLocation():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("https://www.nlb.gov.sg/main/home")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "Home"

    # waits 0.5s if elements are not immediately present before searching
    driver.implicitly_wait(0.5)

    # --- Social Link 1 ---
    # search and click the LinkedIn button
    social_media_link = driver.find_element(by=By.CLASS_NAME, value="fa-linkedin");
    social_media_link.click();

    # waits 1s
    driver.implicitly_wait(1);

    # return back to the NLB Website once the linkedin website has loaded
    if driver.current_url == "https://sg.linkedin.com/company/national-library-board":
        driver.back()

    # waits 1s
    driver.implicitly_wait(1);



    # --- Social Link 2 ---
    # search and click the Facebook button
    social_media_link = driver.find_element(by=By.CLASS_NAME, value="fa-facebook");
    social_media_link.click();

    # waits 1s
    driver.implicitly_wait(1);

    # return back to the NLB Website once the facebook website has loaded
    if driver.current_url == "https://www.facebook.com/nlbsingapore":
        driver.back()

    # waits 1s
    driver.implicitly_wait(1);



    # --- Social Link 3 ---
    # search and click the Instagram button
    social_media_link = driver.find_element(by=By.CLASS_NAME, value="fa-instagram-square");
    social_media_link.click();

    # waits 1s
    driver.implicitly_wait(1);

    # return back to the NLB Website once the Instagram website has loaded
    if driver.current_url == "https://www.instagram.com/nlbsingapore":
        driver.back()

    # waits 1s
    driver.implicitly_wait(1);



    # --- Social Link 4 ---
    # search and click the Facebook button
    social_media_link = driver.find_element(by=By.CLASS_NAME, value="fa-youtube");
    social_media_link.click();

    # waits 1s
    driver.implicitly_wait(1);

    # return back to the NLB Website once the youtube website has loaded
    if driver.current_url == "https://www.youtube.com/c/nlbsg":
        driver.back()



    # --- Social Link 4 ---
    # search and click the Twitter button
    social_media_link = driver.find_element(by=By.CLASS_NAME, value="fa-twitter");
    social_media_link.click();

    # waits 1s
    driver.implicitly_wait(1);

    # return back to the NLB Website once the twitter website has loaded
    if driver.current_url == "https://twitter.com/nlbsingapore":
        driver.back()

    # waits 1s
    driver.implicitly_wait(1);

    driver.quit()
