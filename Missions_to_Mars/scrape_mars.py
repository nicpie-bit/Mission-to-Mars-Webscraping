from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from splinter import Browser
import pandas as pd
from flask import Flask

def scrape():
    #Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Visit url 
    url = "https://redplanetscience.com"
    browser.visit(url)

    #Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Get latest news article info
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text 

    #Visit new url
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)

    html = browser.html
    soup = bs(html, "html.parser")

    #scrape for mars img
    mars_img = soup.find('img', class_="headerimage fade-in").get('src')
    featured_img_url = jpl_url+mars_img

    #scrape mars fact table
    facts_url = "https://galaxyfacts-mars.com"
    mars_facts_table = pd.read_html(facts_url)
    fact_df = mars_facts_table[0]
    fact_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    html_table = fact_df.to_html()
    fact_html_table = html_table.replace('/n', '')

    #scrape for Mar's hemispheres
    

