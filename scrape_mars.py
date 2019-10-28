import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
#import pymongo



def scraping():
    scrape_dict={}
    urx="https://mars.nasa.gov/news/"
    html = requests.get(urx)
    bsobj = bs(html.content, "html.parser")
    result_features = bsobj.find_all('div', class_="features")
    result_titles=result_features[0].find_all("div",class_="content_title")
    result_parag=result_features[0].find_all("div",class_="rollover_description_inner")

    # //Loop through returned results
    title_list=[]
    parag_list=[]
    for result_t in result_titles:
        title_list.append(result_t.a.text)       
    for result_p in result_parag:
        parag_list.append(result_p.text)

    news_title=[]
    title_list
    for title in title_list:
        news_title.append(title.strip("\n"))

    news_p=[]
    parag_list
    for parag in parag_list:
        news_p.append(parag.strip("\n"))

    #--------------------------------------------------------
    #--------------------------------------------------------
    #!which chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'http://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    htmlx = browser.html
    soup = bs(htmlx, 'html.parser')
    result_dos = soup.find_all(class_="carousel_item")
    result_tres=result_dos[0]
    result_tres = soup.find(class_="button fancybox")
    link=result_tres["data-fancybox-href"]
    featured_image_url='https://www.jpl.nasa.gov/' + link

    #--------------------------------------------------------
    #--------------------------------------------------------
    urt="https://twitter.com/marswxreport?lang=en"
    htmlt = requests.get(urt)

    sopa = bs(htmlt.content, "html.parser")
    result_twit = sopa.find('div', class_="js-tweet-text-container")
    result_twitter=result_twit.text
    mars_wea=result_twitter.split("\n")
    pressure=(mars_wea[3])[0:20]
    mars_weather=mars_wea[1]+", "+mars_wea[2]+", "+pressure
    #--------------------------------------------------------
    #--------------------------------------------------------
    urv="https://space-facts.com/mars/"
    tables = pd.read_html(urv)
    mars_info=tables[1]
    mars_facts=mars_info[0:6]
    mars_facts.columns=["Features","Mars Facts"]
    mars_facts=mars_facts.set_index(["Features"])
    html_table = mars_facts.to_html()
    #--------------------------------------------------------
    #--------------------------------------------------------
    urr="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    htmlr = requests.get(urr)
    suppe = bs(htmlr.content, "html.parser")
    result_dict = suppe.find_all('a', class_="itemLink product-item")

    d={}
    hemisphere_images_url=[]
    for result in result_dict:
            d["title"]=result.find('h3').text
            d["img_url"]='https://astrogeology.usgs.gov' + result.img["src"]
            hemisphere_images_url.append(d.copy())

    browser.quit()
    scrape_dict["hemisphere_images_url"]=hemisphere_images_url
    
    scrape_dict={
        'news_title': news_title,
        "news_p" :  news_p,
        "featured_image_url" : featured_image_url,
        "mars_weather" : mars_weather,
        "html_table" : html_table,
        "hemisphere_images_url" : hemisphere_images_url
    }
    return scrape_dict

scraping()




