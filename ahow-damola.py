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
    print("1) Ade Adedji \n 2) Kip Wright \n 3) Tunde Odeyemi \n 4) Tunji Olatubosun \n 5) Genevieve Kumapley \n 6) Tunde Olugboji \n 7) Bimbola Lawore \n 8) Jide Lawore \n 9) add new speaker")
    speaker = input("enter the number associated with the speaker ")
    '''if input == '9':
        newspeaker = input("enter the new speaker name ")'''
    
    scripture = input("enter the scripture book \n Make sure spelling is correct and capitalize \n use '1 chronicles' rather than '1st chronicles' etc. ")
    chapter = input("enter the chapter")
    v1 = input("enter the first verse")
    v2 = input("enter the last verse")

    driver = webdriver.Chrome(executable_path=r"C:\\Users\Damola Olugboji\Desktop\Projects\foder\chromedriver.exe")
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
     
    if scripture == 'Genesis':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('GEN')
    if scripture == 'Exodus':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('EXO')
    if scripture == 'Leviticus':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ELV')
    if scripture == 'Numbers':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('NUM')
    if scripture == 'Deuteronomy':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('DEU')
    if scripture == 'Joshua':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JOS')
    if scripture == 'Judges':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JDG')
    if scripture == 'Ruth':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('RUT')
    if scripture == '1 Samuel':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1SA')
    if scripture == '2 Samuel':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2SA')
    if scripture == '1 Kings':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1KI')
    if scripture == '2 Kings':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2KI')
    if scripture == '1 Chronicles':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1CH')
    if scripture == '2 Chronicles':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2CH')
    if scripture == 'Ezra':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('EZR')
    if scripture == 'Nehemiah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('NEH')
    if scripture == 'Esther':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('EST')
    if scripture == 'Job':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JOB')
    if scripture == 'Psalms':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('PSA')
    if scripture == 'Proverbs':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('PRO')
    if scripture == 'Ecclesiastes':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ECC')
    if scripture == 'Song of Solomon':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('SNG')
    if scripture == 'Isaiah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ISA')
    if scripture == 'Jeremiah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JER')
    if scripture == 'Lamentations':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('LAM')
    if scripture == 'Ezekiel':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('EZK')
    if scripture == 'Daniel':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('DAN')
    if scripture == 'Hosea':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('HOS')
    if scripture == 'Joel':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JOL')
    if scripture == 'Amos':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('AMO')
    if scripture == 'Obadiah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('OBA')
    if scripture == 'Jonah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JON')
    if scripture == 'Micah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('MIC')
    if scripture == 'Nahum':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('NAM')
    if scripture == 'Habakkuk':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('HAB')
    if scripture == 'Zephaniah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ZEP')
    if scripture == 'Haggai':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('HAG')
    if scripture == 'Zechariah':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ZEC')
    if scripture == 'Malachi':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('MAL')
    if scripture == 'Matthew':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('MAT')
    if scripture == 'Mark':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('MRK')
    if scripture == 'Luke':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('LUK')
    if scripture == 'John':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JHN')
    if scripture == 'Acts':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ACT')
    if scripture == 'Romans':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('ROM')
    if scripture == '1 Corinthians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1CO')
    if scripture == '2 Corinthians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2CO')
    if scripture == 'Galatians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('GAL')
    if scripture == 'Ephesians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('EPH')
    if scripture == 'Philippians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('PHP')
    if scripture == 'Colossians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('COL')
    if scripture == '1 Thessalonians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1TH')
    if scripture == '2 Thessalonians':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2TH')
    if scripture == '1 Timothy':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1TI')
    if scripture == '2 Timothy':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2TI')
    if scripture == 'Titus':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('TIT')
    if scripture == 'Philemon':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('PHM')
    if scripture == 'Hebrews':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('HEB')
    if scripture == 'James':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JAS')
    if scripture == '1 Peter':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1PE')
    if scripture == '2 Peter':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2PE')
    if scripture == '1 John':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('1JN')
    if scripture == '2 John':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('2JN')
    if scripture == '3 John':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('3JN')
    if scripture == 'Jude':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('JUD')
    if scripture == 'Revelation':
        Select(driver.find_element_by_xpath('//*[@id="scripture0"]')).select_by_value('REV')

    driver.find_element_by_name('chapter0').send_keys(chapter)
    driver.find_element_by_name('vsFrom0').send_keys(v1)
    driver.find_element_by_name('vsTo0').send_keys(v2)
    driver.find_element_by_class_name('saveCategoriesButton').click()
    
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
