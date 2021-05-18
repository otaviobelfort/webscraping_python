#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Pegar o conteudo HTML pela URL

url =  "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"

option = Options()
# executa em background
option.headless = True

# mostra a excução na tela
#driver = webdriver.Firefox()

# oculta a excução na tela (background)
#driver = webdriver.Chrome(options=option)
driver = webdriver.Firefox(options=option)

driver.get(url)
#print("get url ...")
time.sleep(5)

#button_cookie = "//div[@class='banner-actions-contanier']//button[@onetrust-accept-btn-handler]"
#driver.find_element_by_xpath("button#onetrust-accept-btn-handler").click()

#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']"))).click()

time.sleep(5)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']")


element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

#Parsear o conteudo HTML por meio do BeaultifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

#  Estruturar o conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)

'''
try:
    driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()
    print("clicou...")

except:
    print("ERROOOOOO")
'''


driver.quit() 