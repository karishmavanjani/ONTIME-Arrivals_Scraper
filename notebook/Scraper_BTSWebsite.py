
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import chromedriver_binary
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

url = "https://transtats.bts.gov/ONTIME/Arrivals.aspx"
variable =0

# create a new Chrome session
#driver= webdriver(browser=("chrome"), chromever="78.0.3904.97")

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

Stats = driver.find_element_by_id('chkStatistics_0').click()


Stats2 = driver.find_element_by_id('chkStatistics_1').click()


Months = driver.find_element_by_id('chkAllMonths').click()

#the below elements are covered by something or could be way inside a table hence require execute
Days = driver.find_element_by_xpath('//*[@id="chkAllDays"]')
driver.execute_script("arguments[0].click();", Days)

Year15 = driver.find_element_by_id('chkYears_28')
Year16 = driver.find_element_by_id('chkYears_29')
Year17 = driver.find_element_by_id('chkYears_30')
Year18 = driver.find_element_by_id('chkYears_31')
Year19 = driver.find_element_by_id('chkYears_32')

driver.execute_script("arguments[0].click();", Year19)
driver.execute_script("arguments[0].click();", Year18)
driver.execute_script("arguments[0].click();", Year17)
driver.execute_script("arguments[0].click();", Year16)
driver.execute_script("arguments[0].click();", Year15)


def get_excel():
 Submit = driver.find_element_by_xpath('//*[@id="btnSubmit"]')
 driver.implicitly_wait(10)
 driver.execute_script("arguments[0].click();", Submit)
 driver.implicitly_wait(10)
 try:
        Save= driver.find_element_by_xpath('//*[@id="DL_CSV"]')
        
        driver.implicitly_wait(10)
        driver.execute_script("arguments[0].click();", Save)
        driver.implicitly_wait(30)    
 except NoSuchElementException:
        print("No data")


Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
while (variable<33):
 variable =variable+1 
 Airline = driver.find_element_by_xpath("//*[@id='cboAirline']/option["+str(variable)+"]").click()
 #.text() doesn't work on xpath
 print(driver.find_element_by_xpath("//*[@id='cboAirline']/option["+str(variable)+"]").get_attribute("value"))
 get_excel()
else:
 print("That's all folks!")

 

 #Previous Attempts AKA Rough Work

 #JetBlue 
#Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[22]').click()
#get_excel()

#Below are alternate functions I tried which failed
# select.select_by_visible_text('DL')
#select_by_visible_text('JFK').click()

#ATAAirlines
# Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
# Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[1]').click()
# get_excel()
# #AirTran Airways 
# Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
# Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[2]').click()
# get_excel()
# #Alaska Airlines
# Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
# Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[3]').click()
# get_excel()
#Allegiant Air
#Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
#Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[4]').click()
#get_excel()
#Aloha Airlines
#Airport = driver.find_element_by_xpath('//*[@id="cboAirport"]/option[266]').click()
#Airline = driver.find_element_by_xpath('//*[@id="cboAirline"]/option[5]').click()
#get_excel()
#America West Airlines 






