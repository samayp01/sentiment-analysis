from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_options.add_argument("--user-data-dir=C:\\Users\\hisam\\Desktop\\UserData")
chrome_options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options=chrome_options)



driver.maximize_window()

driver.get("https://seekingalpha.com/article/4339550-wall-street-breakfast-what-moved-markets?source=all_articles_title")
print(driver.find_element_by_xpath("/html/body").text)

# lnks = driver.find_elements(By.TAG_NAME, "a")


# links_list = []
# print("page", page_number)
# for lnk in lnks:
    
#   title = lnk.text
#   if "Wall Street Breakfast:" in title and "(Podcast)" not in title and "(Video)" not in title:
#     links_list.append(lnk.get_attribute("href"))
#     print(lnk.get_attribute("href"))

        


driver.quit()