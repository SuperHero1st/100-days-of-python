from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

# Set up Edge options
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)
edge_options.add_argument('--ignore-certificate-errors')
edge_options.add_argument('--ignore-ssl-errors')
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--disable-software-rasterizer')
edge_options.add_argument("--inprivate")  # Run in private mode
# edge_options.add_argument("user-data-dir=C:/path/to/your/new/profile")  # Use a clean profile if needed

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

# Initialize bot
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

# Test driver
test_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
test_driver.get('https://www.speedtest.net/')
go_button = test_driver.find_elements(By.CLASS_NAME, 'start-button')
for element in go_button:
    print(element)