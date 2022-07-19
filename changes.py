from selenium import webdriver
import datetime

a = input("Enter the URL to take screenshot--:\n") #Taking input from the user
driver =  webdriver.Chrome(executable_path=r"C:\Users\roysh\OneDrive\Desktop\ss.py\chromedriver.exe") #add the path of your chromium headless browser. 
driver.get(a)

#Giving the file name of screenshot

date_stamp = str(datetime.datetime.now()).split('.')[0]
date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
file_name = date_stamp + ".png"
driver.save_screenshot(r"C:\Users\roysh\OneDrive\Desktop\newshot/" + file_name)


driver.close() #closing the headless broweser.
