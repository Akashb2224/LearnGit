from selenium import webdriver

#setup chrome driver 
webdriver driver = new chromedriver()

#navigate youtube
driver.get("www.youtube.com")

driver.findelement(by.class("//input[@type='email']")).sendkeys("qatesting197@gmail.com")

driver.click(by.linktext("Next"))

driver.findelement(by.class("//input[@class='whsOnd zHQkBf' and @type='password']")).sendkeys("Qa$Testing_75 ")

//*[@id="passwordNext"]/div/button/span

