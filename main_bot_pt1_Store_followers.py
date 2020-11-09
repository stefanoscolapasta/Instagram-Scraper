from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time, random

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

username = 'TypeYourUsernameHere'
password = 'TypeYourPasswordHere'
url = 'https://www.instagram.com'
browser = webdriver.Chrome(executable_path='PutPathToChromeDriverHere')

browser.get(url)
login(username, password)
click_non_ora()
search_bar = browser.find_element_by_class_name('TqC_a')
search_bar.click()
search_bar_due = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar_due.send_keys('TypeAccountUsernamenToScrapeHere')
time.sleep(2)
sclViVe_clicca = browser.find_element_by_class_name("z556c").click()
time.sleep(2)
follower_clicca = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').click()
time.sleep(4)

fBody  = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")


    #browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    #browser.execute_script('arguments[0].scrollIntoView()', fBody)
time.sleep(1)
last_ht = 0
ht = 1

while last_ht != ht:
    try:
        last_ht = ht
        num = random.uniform(1,2)
        time.sleep(num)
        ht = browser.execute_script('arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;', fBody)
    except:
        print("Scrolling fucked up")


links = fBody.find_elements_by_tag_name('a')
nomi = []
for link in links:
    if link != '':
        gente = link.get_attribute("href")
        nomi.append(gente)
print(nomi)
with open('ListaInsta.txt', 'w') as f:
    for item in nomi:
        f.write("%s\n" % item)

print("ended")
