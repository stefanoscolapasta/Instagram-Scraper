from selenium import webdriver
from stem import Signal
from stem.control import Controller
from splinter import Browser
import time
import pickle, random

proxyIP = "127.0.0.1"
proxyPort = 9150

proxy_settings = {"network.proxy.type": 1,
                  "network.proxy.ssl": proxyIP,
                  "network.proxy.ssl_port": proxyPort,
                  "network.proxy.socks": proxyIP,
                  "network.proxy.socks_port": proxyPort,
                  "network.proxy.socks_remote_dns": True,
                  "network.proxy.ftp": proxyIP,
                  "network.proxy.ftp_port": proxyPort
                  }
browser = Browser('firefox', profile_preferences=proxy_settings)
browser.visit("http://www.icanhazip.com")

def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


fo = open("PathToTxtFileCreatedWithPreviousBot", "r")
link_persone = fo.readlines()

def login(username, password):
    time.sleep(2)
    username_button = browser.find_element_by_name("username")
    username_button.send_keys(username)
    password_button = browser.find_element_by_name("password")
    password_button.send_keys(password)
    accedi_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
    accedi_button.click()

def click_non_ora():
    time.sleep(3)
    non_ora_button = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

username = 'YourUsername'
password = 'YourPassword'
url = 'https://www.instagram.com'
browser = webdriver.Chrome(executable_path='TypePathToChromeDriver')
browser.get(url)
login(username, password)
time.sleep(1)
click_non_ora()
#getsCookies
pickle.dump(browser.get_cookies() , open("InstaCookie.pkl","wb"))
nPriv = 0
followerSCL = []
SeguitiDelFollowerNum = 0
for link_persona in link_persone:
    switchIP()
    browser.get(link_persona)
    #ributta  i cookie dentro
    for cookie in pickle.load(open("InstaCookie.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']
        browser.add_cookie(cookie)
    num = random.uniform(1, 2)
    time.sleep(num)
    try:
        seguiti_clicca = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(4)

        fBody = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")

        # browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        # browser.execute_script('arguments[0].scrollIntoView()', fBody)
        time.sleep(1)
        last_ht = 0
        ht = 1
        #questo scrolla finchè non si blocca o arriva in fondo
        while last_ht != ht:
            try:
                last_ht = ht
                num = random.uniform(1, 2)
                time.sleep(num)
                ht = browser.execute_script(
                    'arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;', fBody)
            except:
                print("Scrolling s'è fottuto")
        #trova i link ai profili dei follower
        links = fBody.find_elements_by_tag_name('a')
        SeguitiDaiFollower = []
        for link in links:
            if link != '':
                gente = link.get_attribute("href")
                SeguitiDaiFollower.append(gente)
        print(SeguitiDaiFollower)
        SeguitiDelFollowerNum = SeguitiDelFollowerNum +1
        with open(f'ListaSeguitiFollower{SeguitiDelFollowerNum}.txt', 'w') as f:
            for item in SeguitiDaiFollower:
                f.write("%s\n" % item)

        print("ended")

    except:
        nPriv = nPriv + 1
        print(f"profilo privato numero {nPriv}")

    followerSCL.append(SeguitiDaiFollower)
