from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import re

'''
    scrapeHP.py collects links at HP STore homepage by looking for 'a' tag and write the urls in HP_homepage_links.txt
'''

# Homepage of HP Store
url='https://store.hp.com/us/en'

options = webdriver.ChromeOptions()
options.add_argument('headless')
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(chrome_options=options, desired_capabilities=capa)
driver.set_window_size(1440,900)
driver.get(url)
time.sleep(20)

# Get all the link elements at HP Store homepage
sources = driver.find_elements_by_tag_name('a')
link_list=[]
for source in sources:
    try:
        # Get all links' url by href because every link has 'href' attribute but not necessarily has 'text' or 'class'.
        # Noted that get_attribute('href') only return absolute path. To get relative path,
        # pass in 'outerHTML' as attribute then parse the result.
        href = source.get_attribute('href')
        # Get unique links with absolute paths and exclude links with javascript generated
        if re.match('http',href) and href not in link_list:
            link_list.append(href)
            print(href)
    except:
        pass

# Create a txt file and write in all links from above seperated by line break
hphomepage = open('HP_homepage_links.txt', 'wt')
for link in link_list:
        hphomepage.write(link+'\n')
hphomepage.close()