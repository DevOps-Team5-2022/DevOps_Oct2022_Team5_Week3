import time
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_FeedbackForm():
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

def test_SociaMediaLink():
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

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "Home"



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

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "Home"



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

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "Home"



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

def test_libLocation():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("https://www.nlb.gov.sg/main/home")
    
    # Locate library location dropdown
    libDropDown = driver.find_element(by=By.ID, value = "select-lib-button")
    libDropDown.click()

    # Select element with xpath to locate the exact are you wish to select
    libSelect = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/section[2]/div/div/div[1]/div/div/h3/div[1]/div/ul/li[23]/a")
    libSelect.click()
    

    locationForm = driver.find_element(by=By.CLASS_NAME, value = "buttonLibrary")
    locationForm.click()

    # Check page title to see if page has been changed
    libTitle = driver.title
    assert libTitle == "Sengkang Public Library"

    driver.quit()

