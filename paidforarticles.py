from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from keep_alive import keep_alive
from fake_useragent import UserAgent
import random
from selenium.webdriver.common.keys import Keys


def test(proxy):
  ua=UserAgent()
  agent=ua.ie
  chrome_options=webdriver.ChromeOptions()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument("user-agent="+agent)  
  chrome_options.add_argument("window-size=1400,600")
  chrome_options.add_argument('--disable-dev-shm-usage')

  #chrome_options.add_argument('--headless')
  prefs = {"profile.default_content_setting_values.geolocation" :2}
  chrome_options.add_experimental_option("prefs",prefs)
  chrome_options.add_argument('--proxy-server=%s' % proxy)

  driver=webdriver.Chrome(chrome_options=chrome_options)
  try:
    try:

      driver.get("https://factfiest24.blogspot.com/2021/03/top-10-facts-about-india_5.html")
      print('Loaded...')
      driver.find_element_by_xpath('//*[@id="post-body"]/span[2]/a').click()

      driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[1]/a')
      header=driver.find_element_by_xpath('/html/body')

      for i in range(random.randint(12,18)):
        for i in range(random.randint(12,20)):
          header.send_keys(Keys.ARROW_DOWN)
        time.sleep(random.randint(7,12))

      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(random.randint(2,7))

    except:
      pass
          
  finally:
    driver.quit()



      
                    #PROXY code
def scraping():

    try:
       url='https://www.sslproxies.org/'
       r=requests.get(url)


       soup=BeautifulSoup(r.content,'html5lib')

       tbody=soup.find('tbody')

       tr=tbody.findAll('tr')

       for i in tr:
           td=i.findAll('td')
            
           if (td[4]).text=='elite proxy':
               proxy=(td[0].text+':'+td[1].text)
               print(proxy)
               
               try:
                   print("pass proxy to function")
                   test(proxy)
               except:
                   print('failed, trying another proxy')

    except Exception as e:
        print(e)
        time.sleep(10)
        scraping()

keep_alive()

while True:
  try:
    scraping()
  except:
    pass
