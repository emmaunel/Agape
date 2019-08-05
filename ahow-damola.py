import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

"""
def rename():
    return null
"""
driver = webdriver.Chrome(
    executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe"
)
driver.get("https://audio-joiner.com/")
# add path to podcast intro
pathtointro = r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\mak.mp3"
# path to message should be the same as the path to the rename file
# pathtomessage =
driver.find_element_by_class_name("file-input").send_keys(pathtointro)
driver.find_element_by_class_name("btn-save").click()

time.sleep(60)
for a in driver.find_elements_by_xpath(".//a"):
    print(a.get_attribute("href"))

