from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
import time
import os
import re
#TODO: Check if a file exist or not
#TODO: Prevent session from closing
#TODO: Add pretty and useful messages
def main():
    chromedriver ='chromedriver'
    mp3_location = "H:\\New Chruch\\2019\\8)August"
    week_location = 'Week 1'
    driver = webdriver.Chrome(executable_path=chromedriver)
    #chrome_options.add_experimental_options("detach", True)
    driver.get('http://audio-joiner.com')
    time.sleep(3)
    add_button = driver.find_element_by_class_name('file-input')
    # Add the intro
    add_button.send_keys(r"H:\New Chruch\Podcast Intro Revised MP3.mp3")
    # To trick the browser to think it is a person
    time.sleep(3)
    # Gets the message - just write the name, .mp3 will be appended to it
    os.chdir(mp3_location + '\\' + week_location)
    user_input = input("Enter the name of the mp3 file: ")
    user_test = mp3_location + '\\' + week_location + '\\' + user_input + '.mp3'
    print(user_test)
    time.sleep(3)
    add_button.send_keys(user_test)
    time.sleep(3)
    # Join button
    join_button = driver.find_element_by_class_name('save-label')
    join_button.click()
    # Incase the joining takes long
    time.sleep(5)
    # Download the new file
    download_btn = driver.find_element_by_link_text('Download')
    link = download_btn.get_attribute('href')
    print(link)
    time.sleep(5)
    print("Downloading..... to ???")
    
    
    
main()
