import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.com/Sony-ILCE7SM2-mount-Camera-Full-Frame/dp/B0158SRJVQ/ref=pd_sbs_421_1/137-0827430-4405201?_encoding=UTF8&pd_rd_i=B0158SRJVQ&pd_rd_r=3864788c-f131-4829-bf95-c3474e64186c&pd_rd_w=04aRe&pd_rd_wg=p7cCC&pf_rd_p=ed1e2146-ecfe-435e-b3b5-d79fa072fd58&pf_rd_r=HJWRB7QNR44TD8XTT9W3&psc=1&refRID=HJWRB7QNR44TD8XTT9W3'
# my user agent
headers  = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}


page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

#    print(soup.prettify())
title = soup.find(id = "productTitle")
print(title)
print(title)
print(title)
print(title)







"""
import pandas as pd
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
browser = webdriver.Chrome()
browser.get(url)
"""
