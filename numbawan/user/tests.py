import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

class Testfrontend(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_nav_bar_elements(self):
        logging.info("Testing Navbar Elements...")
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "header")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Home')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Menu')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'About')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login')]")) and 
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'User Name Logged')]"))
        )
        navbar = self.driver.find_element(By.ID, "header")
        home = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]")
        menu = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Menu')]")
        about = self.driver.find_element(By.XPATH, "//*[contains(text(), 'About')]")
        login = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Login')]")
        user_name_logged = self.driver.find_element(By.XPATH, "//*[contains(text(), 'User Name Logged')]")
        assert navbar.is_displayed(), "Navbar is not displayed on the page"
        assert home.is_displayed(), "Home is not displayed on the page"
        assert menu.is_displayed(), "Menu is not displayed on the page"
        assert about.is_displayed(), "About is not displayed on the page"
        assert login.is_displayed(), "Login is not displayed on the page"
        assert user_name_logged.is_displayed(), "User Name Logged is not displayed on the page"

class TestNavigations(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_Nav_Links(self):
        logging.info("Testing Navigation Links & Clicking (Maximize window)...")
    # def test_nav_links(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.minimize_window()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Home')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Menu')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'About')]")) and
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Login')]"))
        )

        # Finding the menu link
        menu = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Menu')]")
        # Clicking the menu link
        menu.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/menu/", "Navigation to Menu page failed")
        
        # Finding the home link
        home = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Home')]")
        # Clicking the home link
        home.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/", "Navigation to Home page failed")
        
        # Finding the about link
        about = self.driver.find_element(By.XPATH, "//*[contains(text(), 'About')]")
        # Clicking the about link
        about.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/about/", "Navigation to About page failed")
        
        # Finding the login link
        login = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Login')]")
        # Clicking the login link
        login.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/login/", "Navigation to Login page failed")
        
        # Finding the register(Create new Account)
        Register = self.driver.find_element(By.LINK_TEXT, "Create new account")
        # Clicking the register link
        Register.click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/register/", "Navigation to Register page failed")
        
        # Finding the user name logged link
        #user_name_logged = self.driver.find_element(By.LINK_TEXT, "User Name Logged")
        # Clicking the user name logged link
        #user_name_logged.click() 
        #assert "User Name Logged" in self.driver.title, "Navigation to User Name Logged page failed"

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_home_page(self):
        logging.info("Testing Home Page...")
        self.driver.get("http://127.0.0.1:8000/") 
        self.assertIn("Kopitler", self.driver.title)
        # Locating the Home Header 
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Home Header')]"))
    )
        header_element = self.driver.find_element(By.TAG_NAME,"h1")
        header_text = header_element.text 
        self.assertEqual(header_text, "Home Header")         
          
        # Locating the view menu 
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'View Menu')]"))
        )
        view_menu = self.driver.find_element(By.XPATH, "//*[contains(text(), 'View Menu')]")
        # Clicking the view menu button
        view_menu.click()
        # Checking the url after the view menu button
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/menu/", "Navigation to the Menu Page failed") 
        
class TestAboutPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
                
    def test_about_page(self):
        logging.info("Testing About Page...")
        self.driver.get("http://127.0.0.1:8000/about") 
        self.assertIn("About Us", self.driver.title)
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'About Header')]"))
    )
        header_element = self.driver.find_element(By.TAG_NAME, "h1")
        header_text = header_element.text
        self.assertEqual(header_text, "About Header")
        
class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_register_page(self):
        logging.info("Testing register....")
        self.driver.get("http://localhost:8000/register/")
        self.assertIn("Register", self.driver.title)
        # Used to wait for the site to load up and locate the each element
        WebDriverWait(self.driver, 8).until(
        EC.presence_of_element_located((By.NAME, "name")) and
        EC.presence_of_element_located((By.NAME, "email")) and
        EC.presence_of_element_located((By.NAME, "birthday")) and
        EC.presence_of_element_located((By.NAME, "phone")) and
        EC.presence_of_element_located((By.NAME, "password1")) and
        EC.presence_of_element_located((By.NAME, "password2"))
    )
        # Registration form input and finding each element
        name_input = self.driver.find_element(By.NAME, "name")
        email_input = self.driver.find_element(By.NAME,"email")
        birthdate_input = self.driver.find_element(By.NAME,"birthday")
        phone_input = self.driver.find_element(By.NAME,"phone")
        password1_input = self.driver.find_element(By.NAME,"password1")
        password2_input = self.driver.find_element(By.NAME,"password2")
        register_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        # Filling up each element in the register form
        name_input.send_keys("Shinroi Uchiha")
        email_input.send_keys("assshin@gmail.com")
        birthdate_input.send_keys("12/12/2000")
        phone_input.send_keys("09123456789")
        password1_input.send_keys("NARUTO22")
        password2_input.send_keys("NARUTO22")
        # Clicking the button
        register_button.click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//form[@action='/register/']"))
        
class TestLoginPage(unittest.TestCase):
     
    def setUp(self):
        self.driver = webdriver.Chrome()
        logging.basicConfig(level=logging.INFO)
        
    def tearDown(self):
        self.driver.quit()
            
    def test_login_page(self):
        logging.info("Testing Login....")
        self.driver.get("http://localhost:8000/login/")  
        self.assertIn("Login",self.driver.title)
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.NAME, "username")) and
        EC.presence_of_element_located((By.NAME, "password"))
    )
        # Login form input and finding each element
        email_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME,"password")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        email_input.send_keys("asshin@gmail.com")
        password_input.send_keys("NARUTO22")
        # Clicking the button
        login_button.click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//form[@action='/login/']"))

if __name__ == "__main__":
    # Test suite to run the desired order of test cases
    suite = unittest.TestSuite()
    suite.addTest(Testfrontend('test_nav_bar_elements'))
    suite.addTest(TestNavigations('test_Nav_Links'))
    suite.addTest(TestHomePage('test_home_page'))
    suite.addTest(TestAboutPage('test_about_page'))
    suite.addTest(TestRegisterPage('test_register_page'))
    suite.addTest(TestLoginPage('test_login_page'))
    
    # Execute the test suite
    unittest.TextTestRunner().run(suite)
