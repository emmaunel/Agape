from selenium import webdriver
import time
import os

#TODO: Optimize it to require less user input, fix the hardcorded strings

def main():
    chromedriver = ''
    # mp3_location = "H:\\New Chruch\\2019\\8)August"
    # week_location = 'Week 1'
    # driver = webdriver.Safari()
    # driver.get('http://audio-joiner.com')
    # time.sleep(3)
    # add_button = driver.find_element_by_class_name('file-input')
    # # Add the intro first
    # add_button.send_keys("H:\New Chruch'\Podcast Intro Revised MP3")
    # # Gets the message - just write the name, .mp3 will be appended to it
    # os.chdir(mp3_location + '\\' + week_location)
    # user_input = input("Enter the name of the mp3 file: ")
    # # fix this
    # print(mp3_location + '\\' + week_location + '\\' + user_input + '.mp3')

    driver = webdriver.Safari()
    driver.get('http://127.0.0.1:3000')
    time.sleep(3)
    dow = driver.find_element_by_link_text('Download')
    print(dow.get_attribute('href'))
    

main()