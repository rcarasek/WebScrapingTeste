import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
import json

# pegar conteudo HTML pela url
url = 'http://www.b3.com.br/pt_br/busca/?query=bbas3'
driver.get(url)

cotacao = driver.find_element_by_xpath("//div[@class='tv-widget-chart__price'])
html_content = cotacao.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html_parser')
table = soup.find_next
