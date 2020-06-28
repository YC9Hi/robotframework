from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re

'''
    test_scrapeHP.py is a testing file for modifying scrapeHP.py
'''

url='https://store.hp.com/us/en'

options = webdriver.ChromeOptions()
options.add_argument('headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capa)
driver.set_window_size(1440,900)
driver.get(url)
time.sleep(20)
sources = driver.find_elements_by_tag_name('a')
link_dict={}
link_list=[]
num=0
for source in sources:
    try:
        outer = source.get_attribute('outerHTML')
        link=outer.split('href')[1].split('"')[1].replace('amp;',"")
        if not re.match('java',link) and link not in link_list:
            link_list.append(link)
            print(link)
    except:
        pass
hphomepage = open('HP_homepage_links.txt', 'wt')
for link in link_list:
        hphomepage.write(link+'\n')
hphomepage.close()