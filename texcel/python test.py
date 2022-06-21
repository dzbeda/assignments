from selenium import webdriver
import datetime
import time
import urllib.request
import sys


## Please update your HTTP Link
web_site = 'http://10.164.237.112:30007'
browser = webdriver.Firefox(executable_path = 'C:/Users/texel/geckodriver.exe')
os_datetime= datetime.datetime.now()
os_date = os_datetime.date()


response = urllib.request.urlopen(web_site)
site_status = response.getcode()
#print(site_status)
if site_status == 200:
    print('site is up')
else :
    sys.exit


driver = webdriver.Firefox()
driver.get(web_site)
time.sleep(10)
p_element = driver.execute_script("return date")
#print(p_element)
#print(os_date)

if str(os_date) == str(p_element):
    print('dates are sync')
else:
    print('your host is not sync with web-server')

