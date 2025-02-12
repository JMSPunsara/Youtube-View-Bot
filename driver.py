import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser):
    """Initialize the correct WebDriver based on the browser choice"""
    if browser.lower() == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Chrome(service=service, options=options)

    elif browser.lower() == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError("Unsupported browser! Use 'chrome' or 'firefox'.")

class Bot:
    """Handle interactions with YouTube video"""

    def __init__(self, website, browser):
        """Initialize WebDriver and required parameters"""
        self.driver = get_driver(browser)
        self.website = website  
        self.wait = WebDriverWait(self.driver, 10)
        self.presence = EC.presence_of_element_located
        self.visible = EC.visibility_of_element_located

    def get_vid(self):
        """Open the YouTube link"""
        self.driver.get(self.website)
    
    def play_video(self):
        """Click on the play button"""
        try:
            self.wait.until(self.visible((By.CLASS_NAME, "ytp-large-play-button")))
            play_button = self.driver.find_element(By.CLASS_NAME, "ytp-large-play-button")
            play_button.click()
        except Exception as e:
            print(f"Error clicking play button: {e}")

    def clear_cache(self):
        """Clear the browser cache"""
        self.driver.delete_all_cookies()
    
    def refresh(self):
        """Refresh the page"""
        self.driver.refresh()
    
    def switch_tab(self, tab):
        """Switch to the specified tab"""
        self.driver.switch_to.window(self.driver.window_handles[tab])
    
    def new_tab(self):
        """Open a blank new tab"""
        self.driver.execute_script("window.open('about:blank');")
    
    def close_browser(self):
        """Close the browser"""
        self.driver.quit()
