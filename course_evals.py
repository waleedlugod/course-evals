from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = input("Enter username: ")
password = input("Enter password: ")
driver = webdriver.Firefox()
driver.get("https://aisis.ateneo.edu/j_aisis/displayLogin.do")

# signs in
navElem = driver.find_element(By.NAME, "userName")
navElem.clear()
navElem.send_keys(username)
navElem = driver.find_element(By.NAME, "password")
navElem.clear()
navElem.send_keys(password)
driver.find_element(By.NAME, "submit").click()

# navigate to evals
driver.find_element(By.LINK_TEXT, "COURSE AND FACULTY EVALUATION").click()

# evals
while(True):
    try:
        radios = WebDriverWait(driver, 99999).until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for radio in radios:
            if radio.get_attribute("value") == "5": radio.click()
        
        textareas = driver.find_elements(By.TAG_NAME, "textarea")
        for textarea in textareas:
            textarea.send_keys("N/A")
    except:
        driver.quit()

    try:
        WebDriverWait(driver,
                      99999).until(EC.presence_of_element_located((By.XPATH, "//td[text()='Not Submitted']")))
    except:
        driver.quit()
