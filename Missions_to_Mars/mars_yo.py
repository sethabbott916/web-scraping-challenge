#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import time


# In[2]:

def scrape_info():

    dictionary = {}

    news_url="https://mars.nasa.gov/news/"
    response = requests.get(news_url)

    time.sleep(1)
    # In[3]:

    news_soup = BeautifulSoup(response.text, 'html.parser')
    print(news_soup.prettify())

    # In[4]:

    news_title = news_soup.find(class_="content_title").text
    print(news_title)
    dictionary["news_title"] = news_title


# In[5]:
    news_p=news_soup.find(class_="rollover_description_inner").text
    print(news_p)
    dictionary["news_p"] = news_p

    


# In[6]:



    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    time.sleep(1)

    browser.find_by_id('full_image').click()

    time.sleep(1)

    browser.links.find_by_partial_text('more info').click()

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    img_url = soup.find("img", class_="main_image")["src"]
    add_url = 'https://www.jpl.nasa.gov/'

    jpl = add_url + img_url
    dictionary["jpl"] = jpl
    


# In[7]:



    time.sleep(2)

    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(2)


    mars_weather = soup.find('div', attrs={'dir':'auto','lang':'en'}, class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0').get_text()
    dictionary["mars_weather"] = mars_weather


# In[8]:



    facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)
    facts_df = tables[0]
    html_table = facts_df.to_html()
    clean_table = html_table.replace('\n', '')
    dictionary["clean_table"] =clean_table


# In[9]:

    prehemi= "https://astrogeology.usgs.gov/"

    time.sleep(2)

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)

    time.sleep(1)



    browser.links.find_by_partial_text("Cerberus Hemisphere Enhanced").click()

    browser.links.find_by_partial_text('Open').click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    raw_cerb_url = soup.find("img", class_="wide-image")["src"]
    cerb_url = prehemi + raw_cerb_url
    cerb_title = soup.find("h2", class_="title").get_text()




    browser.back()




    browser.links.find_by_partial_text("Schiaparelli Hemisphere Enhanced").click()

    browser.links.find_by_partial_text('Open').click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    raw_schi_url = soup.find("img", class_="wide-image")["src"]
    schi_url = prehemi + raw_schi_url
    schi_title = soup.find("h2", class_="title").get_text()




    browser.back()




    browser.links.find_by_partial_text("Syrtis Major Hemisphere Enhanced").click()

    browser.links.find_by_partial_text('Open').click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    raw_syrt_url = soup.find("img", class_="wide-image")["src"]
    syrt_url = prehemi + raw_syrt_url
    syrt_title = soup.find("h2", class_="title").get_text()




    browser.back()



    browser.links.find_by_partial_text("Valles Marineris Hemisphere Enhanced").click()

    browser.links.find_by_partial_text('Open').click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    raw_vm_url = soup.find("img", class_="wide-image")["src"]
    vm_url = prehemi + raw_vm_url
    vm_title = soup.find("h2", class_="title").get_text()

    print(vm_url)
    print(vm_title)
    print(cerb_url)
    print(cerb_title)
    print(schi_url)
    print(schi_title)
    print(syrt_url)
    print(syrt_title)


    # In[10]:


    hemisphere_image_urls = []

    cerb_hemisphere = {"title" : cerb_title, "url" : cerb_url}
    schi_hemisphere = {"title" : schi_title, "url" : schi_url}
    syrt_hemisphere = {"title" : syrt_title, "url" : syrt_url}
    vm_hemisphere = {"title" : vm_title, "url" : vm_url}
    hemisphere_image_urls.append(cerb_hemisphere)
    hemisphere_image_urls.append(schi_hemisphere)
    hemisphere_image_urls.append(syrt_hemisphere)
    hemisphere_image_urls.append(vm_hemisphere)
    dictionary["hemisphere_image_urls"] = hemisphere_image_urls








    return(dictionary)
