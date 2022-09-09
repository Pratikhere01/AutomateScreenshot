from selenium import webdriver


#To execute the path where to save screenshot:
driver = webdriver.Chrome(executable_path=r"C:\Users\roysh\OneDrive\Desktop\ss.py\chromedriver.exe")

#The url that we want to take Screenshot:
driver.get("https://www.quora.com/")

#Giving the file name of screenshot:
driver.save_screenshot(r"C:\Screenshot\filename.png")
