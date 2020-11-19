import requests
from bs4 import BeautifulSoup
URL = 'https://www.bcb.gov.br/'
# my user agent
headers  = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


page = requests.get(URL, headers = headers)
print(page)


"""
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
browser = webdriver.Chrome()
browser.get(url)
"""
