from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def swipe():
	
	options = webdriver.ChromeOptions() 
	options.add_argument("user-data-dir=\home\will\.config\google-chrome\Profile 1") #Path to your chrome profile
	options.add_experimental_option("detach", True)

	driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
	driver.get("http://tinder.com")

	elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="c849239686"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')))
	elem = driver.find_element_by_xpath('//*[@id="c849239686"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button')

	while True:
		elem.click()

if __name__ == '__main__':
	swipe()