from selenium import webdriver
import time

def open_driver():
  chrome_options=webdriver.ChromeOptions()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  prefs = {"profile.managed_default_content_settings.images": 2}
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_experimental_option("prefs", prefs)
  #chrome_options.add_argument("--incognito")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-notifications")
  #chrome_options.add_argument('--headless')
  chrome_options.add_extension('C://Python27//vpn.crx')
  driver=webdriver.Chrome(chrome_options=chrome_options)
  str(input('Enter'))
"""
  return driver

def main(driver):  
    try:
        driver.implicitly_wait(5)
        driver.get('https://jungleofferwall.com/offerwall/5/220005471?type=nightfallnews')
        print('Url Opened')
    except:
        main(driver)
        
    return driver


                    
def loop(driver):
    try:
        next_button=driver.find_element_by_id('nextButton')
        
        num=driver.find_element_by_xpath('//*[@id="progressbar-text"]/span')
        print(num.text)
        

        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        driver.find_element_by_id("nextButton").click()
        print('Scrolled and clicked on Next Button')
        print('one slideshow complete')
        time.sleep(12)
        
    except:
      try:
        print('Cant find next button.... clicking on any post ')#problem
        post=driver.find_element_by_id('outbrain_widget_0"]/div/div[1]/ul[1]/li[1]/a/span[1]/img')
        driver.execute_script("arguments[0].scrollIntoView();", post)
        
        driver.find_element_by_xpath('//*[@id="outbrain_widget_0"]/div/div[1]/ul[1]/li[1]/a/span[1]/img').click()
        time.sleep(2)
        window_handles=driver.window_handles
        driver.switch_to.window(window_handles[1])
                
        driver.close()
        driver.switch_to.window(window_handles[0])
        time.sleep(2)
        next_button=driver.find_element_by_id('nextButton')
        loop(driver)
      except:
        try:
          print('nothing happen on clicking on post')
          compleate=driver.find_element_by_xpath('//*[@id="content_container_wraper"]/div[2]/div[1]/div/div[2]/div/a')
          driver.execute_script("arguments[0].scrollIntoView();", compleate)
          driver.find_element_by_xpath('//*[@id="content_container_wraper"]/div[2]/div[1]/div/div[2]/div/a').click()
          print('Fully Complete 0.0214 creadit!')
          
        except:
          main(driver)

driver=open_driver()
driver=main(driver)
while True:
    loop(driver)
    """
open_driver()
