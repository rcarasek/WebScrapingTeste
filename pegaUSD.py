
import pandas as pd
from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
import json


import requests
from selenium import webdriver
url = 'https://www.bcb.gov.br/'
browser = webdriver.Chrome()
browser.get(url)

# my user agent
# https://www.google.com/search?q=my+user+agent&oq=my+user+&aqs=chrome.1.69i57j0l2j0i22i30j0i10i22i30j0i22i30l2j69i60.3479j0j1&sourceid=chrome&ie=UTF-8
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36
