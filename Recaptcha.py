from selenium import webdriver
import time
import urllib
import requests

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_extension('C://Python27//vpn.crx')
chrome_options.add_argument('--proxy-server=%s' % '216.177.227.123')
driver=webdriver.Chrome(chrome_options=chrome_options)
str(input('Enter'))
driver.get('https://www.google.com/recaptcha/api2/demo')

def a():
  iframe = driver.find_element_by_tag_name('iframe')
  driver.switch_to.frame(iframe)
  driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click()
  driver.switch_to.parent_frame()
  try:
    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[2]/div[4]/iframe'))
  except:

    driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[2]/div[2]/iframe'))


  time.sleep(5)
  driver.find_element_by_id('recaptcha-audio-button').click()
  time.sleep(2)
  href = driver.find_element_by_class_name("rc-audiochallenge-tdownload-link").get_attribute("href")
  print(href)
  time.sleep(5)
  urllib.urlretrieve(href,'C:\\Users\\mohd imran\\Desktop\\Downloads\\audio.mp3')
  
a()
driver.execute_script('''window.open("","_blank")''')
driver.switch_to.window(driver.window_handles[1])
driver.get("https://speech-to-text-demo.ng.bluemix.net/")
audioInput = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
audioInput.send_keys('C:\\Users\\mohd imran\\Desktop\\Downloads\\audio.mp3')

time.sleep(5)
text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
while text is None:
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div/span')
result = text.text
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(result)
