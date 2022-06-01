from selenium import webdriver
#import pickle
import time
from keep_alive import keep_alive

def start():
  #idforcomment@gmail.com
  options=webdriver.ChromeOptions()
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')

  d=webdriver.Chrome(chrome_options=options)
  
  def a():
    try:
      d.get("https://www.websyndic.com/")
      time.sleep(1)
      d.find_element_by_id("connect_button").click()
      time.sleep(1)
      d.find_element_by_id("login_email").send_keys("idforcomment@gmail.com")
      d.find_element_by_id("login_passwd").send_keys("websyndic.com")
      d.find_element_by_id("connexion").click()
      d.refresh()
      d.maximize_window()
    
    
    
      d.get("https://www.websyndic.com/wv3/?p=visio01")
    
      time.sleep(2)
      d.find_element_by_xpath('//*[@id="main_page"]/div[1]/div[3]/div/div/a').click()
      print("clicked")
      time.sleep(1500)
    finally:
      d.quit()
      print("Restating...")
  a()

      
keep_alive()

while True:
  try:
    start()
  except:
    pass
