from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from IPython.display import HTML


def scrape():
    #SET UP THE BROWSER
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    driver.get(url)

    html= driver.page_source
    soup=bs(html,"lxml")

    wdiv=soup.find('ul', "item_list")
    
    news_title = wdiv.find_all('div', "content_title")[0].text
    news_title_dic={'news_title':news_title}
    #print(news_title)

    news_p = wdiv.find_all('div', "article_teaser_body")[0].text
    news_p_dic={'news_paragraph':news_p}
    #print(news_p)
    #time.sleep(10)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url_jpl="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    driver.get(url_jpl)

    html= driver.page_source
    soup=bs(html,"lxml")

    wdiv_jpl=soup.find('div', class_= "header")
    #print(wdiv_jpl)

    srt_url=url_jpl
    #print(srt_url)
    srt_url_2=srt_url[:-10]
    #print(srt_url_2)

    featured_image_url=srt_url_2+wdiv_jpl.find_all('img')[1]["src"]
    img_url_dic={'featured_image':featured_image_url}
    #print(featured_image_url)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url_mars_facts="https://space-facts.com/mars/"
    driver.get(url_mars_facts)

    html= driver.page_source
    soup=bs(html,"lxml")

    table=soup.find('table', id="tablepress-p-mars-no-2")

    mars_facts = pd.read_html(url_mars_facts)[0]
    mars_facts.columns=["Description","Mars"]
    mars_facts = mars_facts.set_index(["Description"])
    mars_facts=mars_facts.to_html(classes='table table-striped')
    mars_facts_dic={'facts':mars_facts}
    mars_facts_dic
    #HTML(mars_df.to_html(classes='table table-striped'))
    #time.sleep(10)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url_mars_facts="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver.get(url_mars_facts)

    html= driver.page_source
    soup=bs(html,"lxml")

    wdiv_hemi=soup.find('div', class_= "collapsible")
    #print(wdiv_hemi)

    title_lis=[]
    title_hemi = wdiv_hemi.find_all('h3')
    for i in range(len(title_hemi)):
        
        title=title_hemi[i].text
        title_lis.append(title)
        
    #print(title_lis)

    url_cut=url_mars_facts.replace('search/results?q=hemisphere+enhanced&k1=target&v1=Mars', '')

    #print(url_cut)

    hemi_list=[]
    hemi = wdiv_hemi.find_all('a')

    for i in range(len(hemi)):
        hemi_link=url_cut+hemi[i]["href"]
        #print(hemi_link)
        hemi_list.append(hemi_link)
        
    hemi_list_final = pd.unique(hemi_list).tolist()
    hemi_list_final

    image_list=[]
    for img1 in range(len(hemi_list_final)):
        schiapparelli_url=hemi_list_final[img1]
        driver.get(schiapparelli_url)
        html= driver.page_source
        soup=bs(html,"lxml")
        schiapparelli_html=soup.find('div', class_= "downloads")
        schiapparelli_full_image=schiapparelli_html.find_all('li')[0]
        schiapparelli_image=schiapparelli_full_image.find_all('a')[0]["href"]
        #print(schiapparelli_image)
        image_list.append(schiapparelli_image)
    #print(image_list)

    time.sleep(10)



    
    
    test_dic2={'image_mars1':{'title':title_lis[0],'img_url':image_list[0]},
            'image_mars2':{'title':title_lis[1],'img_url':image_list[1]},
            'image_mars3':{'title':title_lis[2],'img_url':image_list[2]},
            'image_mars4':{'title':title_lis[3],'img_url':image_list[3]}}
    #return return_data
    
    a_dic={}
    a_dic={'news_title':news_title_dic,'news_p':news_p_dic,'img':img_url_dic,'hemi_images': test_dic2, 'facts':mars_facts_dic}
  
    time.sleep(10)

    return a_dic
    driver.close()


    

if __name__ == "__main__":
    print(scrape() )