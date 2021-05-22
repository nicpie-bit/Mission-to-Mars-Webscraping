from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
from splinter import Browser
import pandas as pd
from flask import Flask
import time

def scrape():
    try:
        #Set up Splinter
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path, headless=False)

        #Visit url 
        url = "https://redplanetscience.com"
        browser.visit(url)
        time.sleep(3)

        #Scrape page into Soup
        html = browser.html
        soup = bs(html, "html.parser")

        #Get latest news article info
        news_title = soup.find_all('div', class_='content_title')[0].text
        news_p = soup.find_all('div', class_='article_teaser_body')[0].text 
    except Exception as error:
        browser.quit()
        print(error)

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

    #Visit new url 
    general_url = "https://marshemispheres.com/"
    browser.visit(general_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    #scrape for Mar's hemispheres
    items = soup.find_all('div', class_='item')
    urls=[]

    for item in items:
        url = item.find('a', class_='itemLink product-item')['href']
        urls.append(general_url+url)
    
    titles=[]
    img_urls=[]
    hemisphere_image_urls=[]
    for url in urls:
        response = requests.get(url)
        soup = bs(response.text, 'html.parser')
        item_url = soup.find('img', class_='wide-image').get('src')
        img_url = general_url+'/'+item_url
        img_urls.append(img_url)
        title = soup.find('h2', class_='title').text
        titles.append(title)

    for i in range(len(titles)):
        hemisphere_image_url = {
                'title': titles[i], 
                'img_url': img_urls[i]
            } 
        hemisphere_image_urls.append(hemisphere_image_url)
        browser.back()

    #Store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img_url": featured_img_url,
        "fact_html_table": fact_html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    
    #Close browser
    browser.quit()

    #Return results
    return mars_data





