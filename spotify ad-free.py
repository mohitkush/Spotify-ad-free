#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#install all the libraries required through pip or whatever
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
print("give chromedrivers location ,for example C:\\Users\\Hp\\Downloads\\chromedriver\\chromedriver.exe, in case you don't have the drivers refer chromedriver.chromium.org")
take_driver = input("type here: ")
driver = webdriver.Chrome(take_driver)   
link = "https://open.spotify.com/"
url = driver.get(link)
sleep(randint(3,8))
loged_in = input("log in with your credintials and press enter: ")
###below code is automated for log in with facebook
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/header/div[4]/button[2]").click()
#sleep(randint(3,6))
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/a").click()
#sleep(randint(3,6))
#log_id = ""
#pass_id = ""
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(log_id)
#driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(pass_id + Keys.ENTER)

print('Play a damn song')
sleep(randint(15,20))

while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ad = soup.find("div",{"class":"_3773b711ac57b50550c9f80366888eab-scss ellipsis-one-line"})
    y = ad.text
    if y=='Advertisement':
        print("gotcha")
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "chrome.exe":
                volume.SetMasterVolume(0, None)
                sleep(5)
    else:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "chrome.exe":
                volume.SetMasterVolume(1, None)


# In[ ]:





# In[ ]:




