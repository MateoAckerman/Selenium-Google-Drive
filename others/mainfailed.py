from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("C:\Users\JMATM96M\Desktop\Selenium\ChromeDriver\chromedriver.exe")
browser.get("https://drive.google.com/drive/folders/1uBXD7jK3IL4M2BbEV8-8QrX2wEJ9dGQ1")
element = browser.find_element(By.CLASS_NAME, "l-u-Ab-zb-Pn-ve")
element.doubleclick()
element.click()
element = browser.find_element(By.CLASS_NAME, "a-b-Da-d a-b-od-d h-sb-Ic a-b-d a-b-od-d-gc-c")
element.click()


mail_address = ''
password = ''

from selenium import webdriver

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}
driver = webdriver.PhantomJS(desired_capabilities=PHANTOMJS_ARG)

url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.es/'
driver.get(url)

driver.find_element_by_id("Email").send_keys(mail_address)
driver.find_element_by_id("next").click()
driver.find_element_by_id("Passwd").send_keys(password)
driver.find_element_by_id("signIn").click()