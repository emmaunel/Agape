from selenium import webdriver
import time
import os
import wget

# TODO: Prevent session from closing
# TODO: Add pretty and useful messages
# TODO: remind uncle tunji about cronjobs. Do research on sceduling on windows


mp3_location = "H:\\New Chruch\\2019\\8)August\\"
week_location = 'Week 1\\'
file_extention = '.mp3'


def driver():
    chromedriver = 'chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver)
    return driver


def merger(drive, current, new):
    drive.get('http://audio-joiner.com')
    time.sleep(3)
    add_button = drive.find_element_by_class_name('file-input')
    # Add the intro
    add_button.send_keys(r"H:\New Chruch\Podcast Intro Revised MP3.mp3")
    # To trick the browser to think it is a person
    time.sleep(1)

    # Gets the message - just write the name, .mp3 will be appended to it
    os.chdir(mp3_location + week_location)
    # user_input = input("Enter the name of the mp3 file: ")
    user_test = mp3_location + week_location + current + '.mp3'
    print(user_test)
    # time.sleep(2)
    add_button.send_keys(user_test)
    time.sleep(2)
    # Join button
    join_button = drive.find_element_by_class_name('save-label')
    join_button.click()
    # Incase the joining takes long
    time.sleep(5)

    # Download the new file
    download_btn = drive.find_element_by_link_text('Download')
    link = download_btn.get_attribute('href')
    print("The url is  " + link)
    time.sleep(5)
    return download(link, new)


def download(link, new):
    print('Beginning file download with wget module')
    new_location = mp3_location + week_location + new + file_extention
    print("Download location: " + new_location)
    wget.download(link, new_location)
    print('Closing in 10 seconds....')
    # TODO: show a countdown
    return new_location


def uploaded(drive, file):
    drive.get('https://agapehousenj.sermonstudio.net/login')
    time.sleep(3)
    # TODO: Test login creds
    login_btn = drive.find_element_by_class_name('submit_img')
    login_btn.click()
    time.sleep(3)



def userinput():
    # TODO Validate it: if the user enters the extenstion, remove it
    # TODO: Check if a file exist or not
    current_file = input("Enter the name of the message(R_20190804-100106): ")
    if file_extention in current_file:
        # Remove it
        pass

    temp_file = mp3_location + week_location + current_file + file_extention
    if not os.path.isfile(temp_file):
        print("ERROR: File doesn't exit")
        exit(0)
    # removes it from memory
    del temp_file

    new_file = input("What should the new file be named?(August 4th)")
    return current_file, new_file


def main():
    drive = driver()
    current, new = userinput()
    # Merger
    new_location = merger(drive, current, new)
    # Uploader
    uploaded(drive, new_location)


if __name__ == '__main__':
    main()
