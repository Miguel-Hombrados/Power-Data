# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:07:28 2023

@author: Miguel
"""

## Script for scraping data from Red Electrica and downloading the data into a file



import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import pandas as pd


location = "peninsula"
day = 17
month = 1
year = 2011


url = "https://demanda.ree.es/visiona/"+location+"/demandaqh/tablas/"+str(year)+"-"+str(month)+"-"+str(day)+"/1"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.binary_location = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
rows = soup.find('table',attrs={"id":"tabla_evolucion"}).find('tbody').find_all('tr')

date_time = []
real_power = []
forecasted_power = []
programmed_power = []

for row in rows[1:]:
    date_time.append(row.find_all('td')[0].get_text())
    real_power.append(row.find_all('td')[1].get_text())
    forecasted_power.append(row.find_all('td')[2].get_text())
    programmed_power.append(row.find_all('td')[3].get_text())


df = pd.DataFrame(list(zip(date_time,real_power)),
               columns =['date_time', 'real_power'])
df['real_power'] = pd.to_numeric(df['real_power'],errors="ignore")                # Ignore configuration is done to turn '' into Nan.
df['date_time'] = pd.to_datetime(df['date_time'], format='%Y-%m-%d %H:%M')        # Transform dates written as strings into 'datetime' objects

    
# Ejemplo para dibujar datos

plt.plot(df['real_power'])








