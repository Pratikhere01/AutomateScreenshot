#python3 
# automating screenshot using python selenium module. 


from selenium import webdriver
from time import sleep



a = input("Enter the URL to take screenshot--:\n") #Taking input from the user



driver = webdriver.Chrome(executable_path=r"/AutomateScreenshot/chromedriver") #add the path of your chromium headless browser. 


#The url that we want to take Screenshot
driver.get(a)

#Giving the file name of screenshot
driver.save_screenshot(r"C:\Screenshot\a.png")

driver.close() #closing the headless broweser.


