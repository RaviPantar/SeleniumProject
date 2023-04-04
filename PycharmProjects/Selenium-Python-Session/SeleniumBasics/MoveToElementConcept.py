from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get('https://book.spicejet.com/')
time.sleep(12)
#ActionChains(driver).send_keys(Keys.ESCAPE).perform()
Login_ele = driver.find_element(By.XPATH, "//*[contains(text(),'Login / Signup')]")
ActionChains(driver).move_to_element(Login_ele).perform()
SpecialClubMember_ele = driver.find_element(By.XPATH, "//a[contains(text(),'SpiceClub Members')]")
ActionChains(driver).move_to_element(SpecialClubMember_ele).perform()
MemberLogin_ele = driver.find_element(By.LINK_TEXT, "Member Login")
MemberLogin_ele.click()
#ActionChains.drag_and_drop(source,target).perform()
#ActionChains.click_and_hold(source).move_to_element(target).release().perform()
#ActionChains(driver).context_click(element).perform()
#ActionChains(driver).send_keys_to_element(username,'Ravi')
#ActionChains(driver).send_keys_to_element(Password,'Ravi123')
#ActionChains(driver).click(loginbutton).perform()

time.sleep(3)
driver.quit()
