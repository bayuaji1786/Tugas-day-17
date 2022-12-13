import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Verify_login_succesfully(unittest.TestCase):

    def setUp(test): 
        test.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_success_login(test): 
        # steps
        browser = test.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)
    
    def product(test): 
        # steps
        test.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = test.browser
        browser.get("https://www.saucedemo.com/")
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

        browser.add_cookie({"name":"standard_user","domain":"saucedemo.com","value":"secret_sauce"})
        print(browser.get_cookies())
        browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() # klik tombol sign in
        time.sleep(1)



    def test_failed_login_usernamewrong(test): 
        # steps
        browser = test.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)


    def test_failed_login_passwordwrong(test): 
        # steps
        browser = test.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sauc") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

    def test_failed_login_passwordwrong_wrongusername(test): 
        # steps
        browser = test.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"user-name").send_keys("standard_us") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("secret_sau") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"login-button").click() # klik tombol sign in
        time.sleep(1)

   

    
    def tearDown(test): 
        test.browser.close() 

if __name__ == "__main__": 
    unittest.main()