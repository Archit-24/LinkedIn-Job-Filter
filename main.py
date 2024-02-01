from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3792947356&f_AL=true&geoId=102713980&keywords=Python%20Developer&location=India&origin=JOB_SEARCH_PAGE_LOCATION_HISTORY&refresh=true")







