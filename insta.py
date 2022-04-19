from selenium import webdriver

username = input("Enter your username/id: ")
password = input("Enter your password: ")

path = "C:/Users/bhavi/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=path)

driver.get("http://instagram.com")
driver.implicitly_wait(5)

# ============================Login==================================
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
driver.find_element_by_css_selector("button[type=submit]").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()

driver.implicitly_wait(10)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()

# ===================================Scrolll==========================================
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# =================================Like==================================
# driver.find_element_by_class_name("QBdPU.rrUvL").click()

# # # ===================================Comment===============================
# driver.find_element_by_class_name("Ypffh").click()
# driver.find_element_by_class_name("Ypffh").send_keys("Wow its an amazing photo")
# driver.find_element_by_css_selector("button[type=submit]").click()

# ==============================Search and follow===============================
# string = "http://instagram.com/"
# id = input("Enter the userid you want to search and follow: ")

# driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
# driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(id)
# driver.get(string+id)

# driver.implicitly_wait(5)
# driver.find_element_by_class_name("vBF20._1OSdk").click()

# ===================================================Send a message=============================
driver.find_element_by_class_name("xWeGp").click()

driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div").click()
driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Hello how are you?")
driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
