from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

def zagl(proxys):
    try:
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxys)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver=webdriver.Chrome(chrome_options=chrome_options)

        driver.get('https://zee.gl/DwDJmu')
        #main=driver.find_element_by_link_text('People suffering')
        #main.click()
        driver.implicitly_wait(4)
        time.sleep(8)
        driver.execute_script("window.scrollTo(0,200)")
        time.sleep(10)
        Get_Link=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/a')
        Get_Link.click()
        print('Link Clicked ! quiting.....')
        driver.quit()
        
    except Exception as e:
        print(e)
        driver.quit()



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
                   zagl(proxys)
               except Exception as e:
                   print(e)

    except Exception as e:
        print(e)
        time.sleep(10)
        scraping()
        
scraping()

print('waiting to load')
driver.implicitly_wait(4)

close=driver.find_element_by_xpath('/html/body/div/div/div/img')
close.click()

#iframe = driver.find_element_by_xpath("//iframe[@name='Dialogue Window']")

driver.switch_to.default_content()
driver.switch_to.frame('container-29b552ac181cd0b221e0fcc9e06f675422357')

X=driver.find_element_by_xpath('/html/body/div/div/div/img')

X.click()


#elem.send_keys(Keys.CONTROL + "W") 

