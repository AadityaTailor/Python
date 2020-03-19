# # # from selenium import webdriver
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.common.by import By
# # # import time

# # # driver=webdriver.Chrome(r"C:\Users\SONY\Downloads\chromedriver_win32\chromedriver")
# # # driver.get("https://web.whatsapp.com/")
# # # wait=WebDriverWait(driver,600)

# # # target='"Nikunj"'
# # # string="Message sent using Python!!"

# # # x_arg='//span[contains(@title,'+ target + ')]'
# # # target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
# # # target.click()
# # # inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
# # # input_box=wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
# # # # driver.find_element_by_class_name('X7YrQ')

# # # for i in range(75):
# # #     input_box.send_keys(string+Keys.ENTER)
# # #     time.sleep(1)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

driver = webdriver.Chrome(r'C:\Users\SONY\Downloads\chromedriver_win32\chromedriver')

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

target = '"Aditya Ckp"'

string = "This is by python"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print (group_title)
print ("Wait for few seconds")
group_title.click()
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

for i in range(100):
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
driver.close()