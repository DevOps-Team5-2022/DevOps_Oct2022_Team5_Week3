import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def testSubscribe():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.get("https://www.nlb.gov.sg/main/home")

    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    goToForm = driver.find_element(by=By.LINK_TEXT, value="Subscribe Now");
    goToForm.click();

    time.sleep(7.5);

    driver.switch_to.window(driver.window_handles[1]);

    formTitle = driver.title
    assert formTitle == "Subscribe to eNewsletter | FormSG"

    inputEmail = driver.find_element(by=By.ID, value = "609b86404610f70011046c8e");
    submitForm = driver.find_element(by=By.CLASS_NAME, value = "css-122kdz5");
    inputEmail.send_keys("123@gmail.com");
    submitForm.click();
   

    driver.quit()

    
