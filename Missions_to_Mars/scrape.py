from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    #SET UP THE BROWSER
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    driver.get(url)

    html= driver.page_source
    soup=bs(html,"lxml")

    wdiv=soup.find('ul', "item_list")
    
    news_title = wdiv.find_all('div', "content_title")[0].text
    print(news_title)

    news_p = wdiv.find_all('div', "article_teaser_body")[0].text
    print(news_p)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url_jpl="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    driver.get(url_jpl)

    html= driver.page_source
    soup=bs(html,"lxml")

    

    time.sleep(10)
    #return_data = {}
    driver.close()
    #return return_data

if __name__ == "__main__":
    print(scrape_info() )