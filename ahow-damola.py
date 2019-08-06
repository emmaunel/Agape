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

finaudio = (
    r"C:\\Users\Damola Olugboji\Desktop\Projects\Ahow Auto\audiodownload"
)  # path to final audio download


driver = webdriver.Chrome(
    executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe"
)
driver.get("https://audio-joiner.com/")

pathtointro = (
    r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\shotty.mp3"
)  # path to podcast intro
driver.find_element_by_class_name("file-input").send_keys(pathtointro)
driver.find_element_by_class_name("btn-save").click()
# need to add path to message


time.sleep(
    35
)  # allows for load time, there is probably a better way to do this but i'm lazy
# section below allows for the ability to parse links in the html file and find the download link
for a in driver.find_elements_by_xpath(".//a"):
    link = a.get_attribute("href")
    if type(link) == str:
        rlink = link
        if ".mp3" in rlink:
            print(rlink)
            driver.execute_script("window.open('about:blank', 'tab2');")
            driver.switch_to.window("tab2")
            driver.get(rlink)
            time.sleep(15)
            driver.close()

