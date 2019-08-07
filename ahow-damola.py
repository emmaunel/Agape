import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# for now - new series/speakers need to be inputted manually


"""
def rename():
    return null
"""


def studio():

    title = input("enter the sermon title ")
    print(
        "1) Ade Adedji \n 2) Kip Wright \n 3) Tunde Odeyemi \n 4) Tunji Olatubosun \n 5) Genevieve Kumapley \n 6) Tunde Olugboji \n 7) Bimbola Lawore \n 8) Jide Lawore \n 9) add new speaker"
    )
    speaker = input("enter the number associated with the speaker ")

    '''if input == '9':
        newspeaker = input("enter the new speaker name ")'''

    driver = webdriver.Chrome(
        executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe"
    )
    driver.get("https://agapehousenj.sermonstudio.net/login")
    identity = driver.find_element_by_id("identity")
    identity.send_keys("admin@agapehousenj.org")
    driver.find_element_by_id("credential").send_keys("Media123")
    driver.find_element_by_id("submit").click()
    time.sleep(5)
    titlebox = driver.find_element_by_name("title")
    titlebox.send_keys(title)
    add = driver.find_element_by_name("create_new_posting")
    add.click()
    time.sleep(10)
    if speaker == '1':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('217711')#Ade Adedji
    elif speaker == '2':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('226163')#Kip Wright
    elif speaker == '3':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('216941')#Tunde Odeyemi
    elif speaker == '4':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('215248')#Tunji Olatubosun
    elif speaker == '5':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('229403')#Genevieve Kumapley
    elif speaker == '6':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('213970')#Tunde Olugboji
    elif speaker == '7':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('213972')#Bimbola Lawore 
    elif speaker == '8':
        Select(driver.find_element_by_xpath('//*[@id="speaker"]')).select_by_value('213971')#Jide Lawore
    '''elif speaker == '9':
        driver.execute_script("window.open('about:blank', 'tab2');")
        driver.switch_to.window("tab2")
        driver.get('https://agapehousenj.sermonstudio.net/posting/speaker_edit_view')
        driver.find_element_by_name('title').send_keys(newspeaker)
        driver.find_element_by_id('createSeries').click()'''#need to figure a better way to input new speaker
        

    chrome_options.add_experimental_option("detach", True)


def audiojoiner():
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

    # section below allows for the ability to parse links in the html file and find the download link
    done = input("when it is finished type a letter and hit enter ")

    for a in driver.find_elements_by_xpath(".//a"):
        link = a.get_attribute("href")
        if type(link) == str:
            rlink = link
            if ".mp3" in rlink:
                # print(rlink)
                driver.execute_script("window.open('about:blank', 'tab2');")
                driver.switch_to.window("tab2")
                driver.get(rlink)
                break
    studio()


audiojoiner()










"""
217711
Deacon Ade Adedji
226163
Deacon Kip Wright
216941
Deacon Tunde Odeyemi
215248
Deacon Tunji Olatubosun
229403
Deaconess Genevieve  Kumapley
217836
Dr. Alan Miller
227343
Dr. David Schroeder
221075
Dr. Kynan Bridges
225066
Fadekemi Okahim
223640
Femi Awodele
213970
Minister Tunde Olugboji
213972
Pastor Bimbola Lawore
225913
Pastor German Rica
219429
Pastor Ghandi Olaoye
213971
Pastor Jide Lawore
220053
Pastor Ruth Mateola
215912
Rev. Prof. Erhabor
215422
"""
