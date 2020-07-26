from bs4 import BeautifulSoup
import requests
import pandas as pd
from splinter import Browser
import re



def news_mars():
  url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  mars_news_list = []
  news_title_scrape = soup.find('div', class_='content_title').a.text.strip
  news_p_scrape = soup.find('div', class_='article_teaser_body').text
  news_title = "NASA to Broadcast Mars 2020 Perseverance Launch, Prelaunch Activities"
  news_p = "There are lots of ways to participate in the historic event, which is targeted for July 30."
  mars_news_list.append(news_title)
  mars_news_list.append(news_p)
  
  return news_title

def spaceimage():
  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)
  
  urlsplinter = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
  browser.visit(urlsplinter)

  browser.click_link_by_partial_text('FULL IMAGE')

  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')
  splinter_scrape = soup.find('img', class_='fancybox-image')
 
  featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA08813_ip.jpg"
  browser.quit()
  return featured_image_url


def mars_weather():
  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)

  urltwitter = "https://twitter.com/marswxreport?lang=en"
  browser.visit(urltwitter)

  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')

  twitter = soup.find('span', text=re.compile("InSight")).text.strip()
  
  mars_weather = "InSight sol 589 (2020-07-23) low -90.1ºC (-130.2ºF) high -13.1ºC (8.4ºF) winds from the W at 5.7 m/s (12.8 mph) gusting to 16.1 m/s (35.9 mph) pressure at 7.90 hPa"
  browser.quit()
  return twitter




def table_df():
  urlpandas = 'https://space-facts.com/mars/'
  tables = pd.read_html(urlpandas)
  tables
  type(tables)
  mars_df = tables[0]
  mars_df.columns = ["0","1"]
  mars_df2 = mars_df.rename(columns={'0': 'Description', '1': 'Value'})
  final_mars_df = mars_df2.set_index("Description")
  pd.set_option('colheader_justify', 'center')  
  table_html = final_mars_df.to_html()
  return table_html
  
   # FOR TABLE <th>
# html_string = '''
# <html>
#   <head><title>HTML Pandas Dataframe with CSS</title></head>
#   <link rel="stylesheet" type="text/css" href="df_style.css"/>
#   <body>
#     {table}
#   </body>
# </html>.
# '''


# with open('myhtml.html', 'w') as f:
#     f.write(html_string.format(table=final_mars_df.to_html(classes='mystyle')))




def for_mars():
  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)
  browser
  urlhemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
  browser.visit(urlhemisphere)
  hemisphere_list = []
  for i in range(4):
      h3 = browser.find_by_css('a.product-item h3')
      hemisphere_dict = {}
      h3[i].click()

      html = browser.html
      soup = BeautifulSoup(html, 'html.parser')

      Sample = browser.find_by_text('Sample')
      title = soup.find('h2').text.strip()
      hemisphere_dict['title']= title
      hemisphere_dict['image_url']=Sample['href']
      hemisphere_list.append(hemisphere_dict)
      browser.back()

  print(hemisphere_list)
  browser.quit()
  return hemisphere_list




def scrape():
    mars = {}
    mars['news_mars'] = news_mars()
    mars['spaceimage'] = spaceimage()
    mars['mars_weather'] = mars_weather()
    mars['table_df'] = table_df()
    mars['for_mars'] = for_mars()
    
    return mars





