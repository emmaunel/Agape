import os
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# for now - new series/speakers need to be inputted manually
# find way to download to specific folder

"""os.chdir(r'C:\Users\Media\Desktop\sermon auto')
now = datetime.datetime.now()
for f in os.listdir():
    str1 = str(now.year)
    str2 = str(now.month)
    str3 = str(now.day)
    date = (str2 + "-"+ str3 +"-"+ str1 + ".mp3")
    os.rename(f, date)"""


def studio():

    scripture = input("enter the scripture book \n Make sure spelling is correct and capitalize \n use '1 chronicles' rather than '1st chronicles' etc. ")
    chapter = input("enter the chapter")
    v1 = input("enter the first verse")
    v2 = input("enter the last verse")

    driver = webdriver.Chrome(executable_path=r"C:\Users\Media\Desktop\webdriver\chromedriver.exe"
    )
    driver.get("https://agapehousenj.sermonstudio.net/login")
   
    chrome_options.add_experimental_option("detach", True)


def audiojoiner():
    now = datetime.datetime.now()
    str1 = str(now.year)
    str2 = str(now.month)
    str3 = str(now.day)
    date = (" \\" + str2 + "-"+ str3 +"-"+ str1 + ".mp3")    
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Media\Desktop\webdriver\chromedriver.exe"
    )
    driver.get("https://audio-joiner.com/")
    pathtointro = (r"H:\New Chruch\Podcast Intro Revised MP3.mp3")  # path to podcast intro
    pathtosermon = (r"C:\Users\Media\Desktop\sermon auto{}".format(date)) #path to sermon
    print (pathtosermon) #important
    driver.find_element_by_class_name("file-input").send_keys(pathtointro)
    time.sleep(5)
    #driver.find_element_by_class_name("file-input").send_keys(pathtosermon)
    driver.find_element_by_class_name("btn-save").click()

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
