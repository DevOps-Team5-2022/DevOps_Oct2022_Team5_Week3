from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_libLocation():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    submit_button = driver.find_element(by=By.CLASS_NAME, value="buttonLibrary")

    submit_button.click()

    locationTitle = driver.title
    assert locationTitle == "National Library / Lee Kong Chian Reference Library"

    driver.quit()
