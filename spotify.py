def main():
    import os
    import pickle
    from time import sleep
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from random import randint
    from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    link = "https://open.spotify.com/"
    url = driver.get(link)
    sleep(randint(3,8))
    try:
        cookies = pickle.load(open("cookies"+str(os.environ['COMPUTERNAME'])+".pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
    except FileNotFoundError:
        loged_in = input("log in with your credintials and press enter: ")
        pickle.dump( driver.get_cookies() , open("cookies"+str(os.environ['COMPUTERNAME'])+".pkl","wb"))

    print('Play a damn song')
    sleep(randint(10,15))
    while True:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        ad = soup.find("div",{"class":"_3773b711ac57b50550c9f80366888eab-scss ellipsis-one-line"})
        y = ad.text
        if y=='Advertisement':
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "chrome.exe":
                    volume.SetMasterVolume(0, None)
        else:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "chrome.exe":
                    volume.SetMasterVolume(1, None)
    return 0
if __name__ == '__main__':
    main()
