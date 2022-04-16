from selenium import webdriver
import pickle
import time
from keep_alive import keep_alive

def start():
  options=webdriver.ChromeOptions()
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  #options.add_argument("--headless")
  d=webdriver.Chrome(chrome_options=options)
  d.get("http://neon.today")
  cookies=pickle.load(open("neon.pkl", "rb"))
  for cookie in cookies:
    d.add_cookie(cookie)
  def a():
    d.get("http://neon.today/dash/earn")
    try:
      d.find_element_by_id("open").click()
      print("clicked")
    finally:
      print("sleeping")
      time.sleep(1000)
      a()
  a()
keep_alive()
while True:
  try:
    
    start()
    print("1hour complete")
  except:
    pass
