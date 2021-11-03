from selenium import webdriver
from keep_alive import keep_alive
import  time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument("--incognito")
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument("user-data-dir=other")
#chrome_options.add_argument('headless')
print("start")

#chrome_options.add_extension('buster.crx')
driver=webdriver.Chrome(chrome_options=chrome_options)

print('Chromedriver started')
keep_alive()

driver.maximize_window()
url="https://thetimecave.com/funfacts/22-pictures-that-will-instantly-make-your-day/?uid=219413205"
def start():
  global driver
  driver.implicitly_wait(500)
  
  driver.set_page_load_timeout(1000)
  print("opening timecavecontent url")
  driver.get(url)
  print("url opened")
  try:
    driver.set_window_size(978,727)
  except:
    pass
  return driver

def main_loop(driver):
  try:
    driver.implicitly_wait(20)

    def main():
      try:
        print(driver.title)
      
        wait = WebDriverWait(driver, 20)
        print("wait")
        element = wait.until(EC.element_to_be_clickable((By.ID, 'next_slide')))

        print('finded')

        Next=driver.find_element_by_id('next_slide')
        print(element.text)

        driver.execute_script("arguments[0].scrollIntoView();", Next)


        print('scrolled')
        driver.set_page_load_timeout(500)
        try:
          driver.find_element_by_id('next_slide').click()
        except:
          try:
            driver.find_element_by_id('exco_sticky-x-button').click()
            print("Video Removed")
            driver.execute_script("arguments[0].scrollIntoView();", Next)
            driver.find_element_by_id('next_slide').click()
          except:
            driver.refresh()
            main()
        print('clicked')
        
        if driver.title=='Earn':
          print("complete")
          print('Quit...')
          driver.quit()

        elif 'thecontentcave' in driver.title:
          print("One Shlideshow Complete")
          main()

        else:
          driver.set_page_load_timeout(100)
          driver.refresh()
          main()
          
        #driver.get("https://www.factfeast.online/2020/08/71percent-of-earth-we-live-in-is-filled.html?m=1")
      except Exception as e:
        print(e)
        try:
          driver.refresh()
        except:
          driver.refresh()
        main()
    main()

  except Exception as e:
    print(e)
    try:
      driver.refresh()
      main()
    except:
      driver.refresh()
      main()




web_driver=start()

main_loop(web_driver)








"""from selenium import webdriver
#import pickle
#from keep_alive import keep_alive
import  time

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_extension('buster.crx')
#keep_alive()
driver=webdriver.Chrome(chrome_options=chrome_options)

url='https://factfeast.online'
driver.maximize_window()
def start():
  try:
    driver.get(url)
    return driver
  except:
    start()

def main_loop(driver):
  try:
    driver.implicitly_wait(20)
    Next=driver.find_element_by_xpath('//*[@id="next-pre-blow"]/div[2]')
    driver.execute_script("arguments[0].scrollIntoView();", Next)
    time.sleep(20)
    print('clicking on next button')
    driver.find_element_by_xpath('//*[@id="next-pre-blow"]/div[2]').click()
    print('Clicked successfully')
    time.sleep(5)
    if driver.title=='Earn':
      print('complete')
    elif 'thecontentcave' in driver.title:
      print("One Shlideshow Complete")
      main_loop(driver)
    else:
      driver.get(url)
      main_loop(driver)

  except Exception as e:
    print(e)
    driver.get(url)
    main_loop(driver)

driver=start()
main_loop(driver)


'''from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle

chrome_options=webdriver.ChromeOptions()

def start():
    try:
        driver=webdriver.Chrome(chrome_options=chrome_options)
    except:
        start()
    try:
        driver.get('https://faccebook.com/')
        cookies=pickle.load(open('python_facebook.pkl','rb'))       #########Cookies needed########

        for cookie in cookies:
            driver.add_cookie(cookie)

        print('cookie updated!')
        

        driver.implicitly_wait(20)
    except:
        driver.quit()
        start()



def sub_start():
        try:
            driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_timecave_slideshows')

            driver.maximize_window()

            print('window maximized')
            
        except:
            sub_start()

def cookie_iframe():
            try:
                driver.switch_to.frame(driver.find_element(By.ID,'ifrmCookieBanner'))

                driver.find_element_by_class_name('intro-banner-btn').click()

                driver.switch_to.parent_frame()

                driver.find_element_by_xpath('//*[@id="viewTimecaveTOffers"]/tbody/tr/td[5]/div/a/span/input').click()
                
                print('clicked on slideshow')
                window_handles=driver.window_handles
                driver.close()
                
                print('Parent window closed')

                driver.switch_to.window(window_handles[1])

                driver.set_window_size(900,744)

                
                print("driver minimized")

            except:
                sub_start()
        cookie_iframe()
    sub_start()

def timecave_page()
        try:
            for i in range(0,7):
                
                print('Finding element')
                Next=driver.find_element_by_id("next_slide")
                
                print('Element Found')
                driver.execute_script("arguments[0].scrollIntoView();", Next)
                print('Scrolled')
                
                driver.find_element_by_id("next_slide").click()
                print('Clicked On element! compleated.........')
                time.sleep(3)
        except:
            driver.refresh()
            print('Got error in timecaves page trying again after reloding')
            
            timecave_page()
        driver.maximize_window()
    timecave_page()


def reloading():
        try:
            driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_timecave_slideshows')

        except:
            time.sleep(300)
            reloading()
        try:
            driver.switch_to.frame(driver.find_element(By.ID,'ifrmCookieBanner'))
                
            driver.find_element_by_class_name('intro-banner-btn').click()
            driver.switch_to.parent_frame()
                
        except:
            try:
                driver.find_element_by_xpath('//*[@id="viewTimecaveTOffers"]/tbody/tr/td[5]/div/a/span/input').click()
                print('clicked on slideshow')
                    
                window_handles=driver.window_handles

                driver.close()
                print('Parent window closed')

                driver.switch_to.window(window_handles[1])
                driver.set_window_size(900,744)
                    
                print("driver minimized")
                timescave_page()
            except:
                reloading()
                
            sub_start()
    reloading()"""
