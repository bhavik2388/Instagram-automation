from selenium import webdriver

chromepath="C:/Users/bhavi/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chromepath)

driver.get('http://instagram.com/')

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys("your_id")

driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys("password")

driver.find_element_by_css_selector('button[type=submit]').click()

driver.find_element_by_css_selector('button[type=submit]').click()
