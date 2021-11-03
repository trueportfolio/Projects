import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
import time

def PaidForArticle(proxys):
    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--proxy-server=%s' % proxys)
            
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.factfeast.online/2021/03/top-10-facts-about-india_5.html")

        driver.implicitly_wait(4)

        print('Loaded...')
        article_link = driver.find_element_by_link_text('facts about china')
        article_link.click()
        
        try:
            driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[1]/a')
            driver.maximize_window()
            header=driver.find_element_by_xpath('/html/body')
            
            for i in range(random.randint(20,25)):
                for i in range(random.randint(12,25)):
                    header.send_keys(Keys.ARROW_DOWN)
                    time.sleep(random.randint(8,15))
        except:
            pass
    finally:
        driver.quit()
        
                            #PROXCY code
def scraping():

    try:
       url='https://www.sslproxies.org/'
       r=requests.get(url)


       soup=BeautifulSoup(r.content,'lxml')

       tbody=soup.find('tbody')

       tr=tbody.findAll('tr')

       for i in tr:
           td=i.findAll('td')
            
           if (td[4]).text=='elite proxy':
               proxys=(td[0].text+':'+td[1].text)
               print(proxys)
               
               try:
                   print("pass proxy to function")
                   #PaidForArticle(proxys)
               except Exception as e:
                   print('failed, trying another proxy')

    except Exception as e:
        print(e)
        time.sleep(10)
        scraping()
        
scraping()
