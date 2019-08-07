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

def studio():

    title = input("enter the sermon title ")
    print("1) Ade Adedji \n 2) Kip Wright \n 3) Tunde Odeyemi \n 4) Tunji Olatubosun \n 5) Genevieve Kumapley \n 6) Tunde Olugboji \n 7) Bimbola Lawore \n 8) Jide Lawore \n 9) add new speaker")
    speaker = input("enter the number associated with the speaker ")

    driver = webdriver.Chrome(executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe")
    driver.get('https://agapehousenj.sermonstudio.net/login')
    identity = driver.find_element_by_id('identity')
    identity.send_keys('admin@agapehousenj.org')
    driver.find_element_by_id('credential').send_keys('Media123')
    driver.find_element_by_id('submit').click()
    time.sleep(5)
    titlebox = driver.find_element_by_name('title')
    titlebox.send_keys(title)
    add = driver.find_element_by_name('create_new_posting')
    add.click()
    
    el = driver.find_element_by_name('speaker')
    for option in el.driver.find_element_by_tag_name('option'):
        if option.text == '1':
            option.text='217711'
            option.click()
            break
        elif option.text == '2':
            print("okay") 
        elif option.text == '3':
            print("okay") 
        elif option.text == '4':
            print("okay") 
        elif option.text == '5':
            print("okay") 
        elif option.text == '6':
            print("okay") 
        elif option.text == '7':
            print("okay") 
        elif option.text == '8':
            print("okay")
        elif option.text == '9':
            print("okay")  
    
    chrome_options.add_experimental_option("detach", True)



def audiojoiner():
    driver = webdriver.Chrome(executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe")
    driver.get("https://audio-joiner.com/")
    pathtointro = (r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\shotty.mp3")  # path to podcast intro
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
                #print(rlink)
                driver.execute_script("window.open('about:blank', 'tab2');")
                driver.switch_to.window("tab2")
                driver.get(
                    rlink
                )  
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