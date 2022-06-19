from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)



driver.maximize_window()
driver.get("https://seekingalpha.com/author/wall-street-breakfast")

for page_number in range(1, 90):
  

  try:
    # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 10, 4).until(
      EC.presence_of_element_located((By.CLASS_NAME, "row"))
    )
  finally:
    # else quit
    driver.quit()
    print("Reached")
  lnks = driver.find_elements(By.TAG_NAME, "a")


  ran = False
  links_list = []
  print("page", page_number)
  for lnk in lnks:
  
    title = lnk.text
    if "Wall Street Breakfast:" in title and "(Podcast)" not in title and "(Video)" not in title:
      links_list.append(lnk.get_attribute("href"))
      print(lnk.get_attribute("href"))
  

  driver.find_element_by_css_selector('.page-link').click()


      


driver.quit()

with open("links.txt", "a") as f:
  for link in links_list:
    f.write(link + "\n")
    print(link)
