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

    # search and click the Contact Us link
    contact_link = driver.find_element(by=By.LINK_TEXT, value="Contact Us");
    contact_link.click();

    # waits 0.5s if elements are not immediately present before searching
    driver.implicitly_wait(0.5);

    # check that its at NLB Contact Us Page
    contact_title = driver.title
    assert contact_title == "Contact Us";

    # search and click the online link to go Feedback Form
    feedback_link = driver.find_element(by=By.LINK_TEXT, value="online");
    feedback_link.click();

    # waits 7.5s (due to the checking address bar that happens)
    time.sleep(7.5);


    # switch window focus to the new tab
    driver.switch_to.window(driver.window_handles[1]);

    # check that its on the Feedback form page
    feedback_title = driver.title;
    assert feedback_title == "Feedback | FormSG"

    # fill in and submit feedback form
    comment_input = driver.find_element(by=By.ID, value = "60012c16cc381d001141b590");
    name_input = driver.find_element(by=By.ID, value = "600129caba0ee20011f3186f");
    email_input = driver.find_element(by=By.ID, value = "6059a2ec64ab2a0012bd837d");
    #submit_button = driver.find_element(By.XPATH, "//button[@class='chakra-button.css-1qh1fsx']");
    submit_button = driver.find_element(by=By.CLASS_NAME, value = "css-1qh1fsx");
    comment_input.send_keys("Testing Feedback");
    if randint(0, 1) == 0:
        name_input.send_keys("John Doe");
    else:
        name_input.send_keys("Jane Doe");
    email_input.send_keys("Test" + str(randint(100, 999)) + "@gmail.com");
    submit_button.click();

    # waits 2s
    time.sleep(5);

    # complete feedback experience form
    five_star = driver.find_element(by=By.ID, value = "rating-5");
    #five_star.click();
    driver.execute_script("arguments[0].click();", five_star);
    experience_input = driver.find_element(by=By.CLASS_NAME, value = "css-1pymk5v");
    experience_input.send_keys("Great");
    submit2_button = driver.find_element(by=By.CLASS_NAME, value = "css-1qvwnrl");
    submit2_button.click();

    time.sleep(1);

    # check that feedback experience has been successfully sent
    thanks_txt = driver.find_element(by=By.CLASS_NAME, value = "css-1kxrhf3").text;
    assert thanks_txt == "Thank you for submitting your feedback!"
    
    thanks2_txt = driver.find_element(by=By.CLASS_NAME, value = "css-1uz1spc").text;
    assert thanks2_txt == "Thank you! We are looking into your enquiry/feedback."

    back_button_txt = driver.find_element(by=By.CLASS_NAME, value = "css-cmey1v").text;
    assert back_button_txt == "Back to NLB";

    driver.quit()
