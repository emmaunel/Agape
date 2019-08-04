import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#for the podcast

def rename():
    return null

def audiojoiner():
    driver = webdriver.Chrome(r'C:\Users\Media\Desktop\webdriver\chromedriver.exe')
    driver.get('https://audio-joiner.com/')
    driver.find_elements_by_class_name('file-input').send_keys('H:\\New Chruch\Podcast Intro Revised MP3.mp3')
    return driver

def studio():
    return null
    


driver = audiojoiner()