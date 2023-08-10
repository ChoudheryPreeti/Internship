#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.##a python program which searches all the product under a particular product from www.amazon.in.##


# In[30]:


user= input('Enter the product that we want to search : ')


# In[ ]:


2.##scraping the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv##


# In[192]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[193]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[194]:


driver.maximize_window()


# In[195]:


url = "https://www.amazon.in/"
driver.get(url)


# In[196]:


search= driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search.send_keys('guitar')


# In[197]:


search_button=driver.find_element(By.XPATH,'//span[@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]')
search_button.click()


# In[198]:


product_urls=[] 
for i in range(0,3):      
    product_url= driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in product_url:
        product_urls.append(i.get_attribute("href"))
        next_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')


# In[199]:


len(product_urls)


# In[200]:


Brand_name = []
Product_name = []
Prices = []
Exchange = []
Expected_delivery = []
Availability = []

for i in product_urls:
    driver.get(i)
    time.sleep(0)
    
    try:
        brand = driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]')
        Brand_name.append(brand.text)
    except NoSuchElementException:
        Brand_name.append('-')
        
    try:
        product = driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Product_name.append(product.text)
    except NoSuchElementException:
        Product_name.append('-')
        
    
    try:
        price = driver.find_element(By.XPATH,'//span[@class="a-price-whole"]')
        Prices.append(price.text)
    except NoSuchElementException:
        Prices.append('-')

    try:
        exchange = driver.find_element(By.XPATH,'//span[@class="a-size-small a-color-link a-text-normal"]')
        Exchange.append(exchange.text)
    except NoSuchElementException:
        Exchange.append('-')
        
    try:
        delivery = driver.find_element(By.XPATH,'//span[@class="a-text-bold"]')
        Expected_delivery.append(delivery.text)
    except NoSuchElementException:
        Expected_delivery.append('-')

        
    try:
        availability = driver.find_element(By.XPATH,'//span[@class="a-size-medium a-color-success"]')
        Availability.append(availability.text)
    except NoSuchElementException:
        Availability.append('-')


# In[201]:


print(len(Brand_name),len(Product_name),len(Prices),len(Exchange),len(Expected_delivery),len(Availability))


# In[202]:


df= pd.DataFrame({'Brand Name':Brand_name,'Name of the Product':Product_name,'Price':Prices,'Return/Exchange':Exchange,'Expected Delivery':Expected_delivery,'Availability':Availability,'Product URL':product_urls})
df


# In[ ]:


df.to_csv("df.csv")


# In[ ]:


driver.close()


# In[ ]:


3.##Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. ##


# In[15]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import requests
import re
import urllib.request
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[16]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[17]:


driver.maximize_window()


# In[20]:


url = "http://images.google.com/"

urls = []
data = []

search_item = ["Fruits","Cars","Machine Learning","cakes","guitars"]
for item in search_item:
    driver.get(url)
    
    search= driver.find_element(By.XPATH,"//textarea[@class='gLFyf']")
    search.send_keys(str(item))
    
    search_button = driver.find_element(By.XPATH,"//span[@class='z1asCe MZy1Rb']")
    search_button.click()
    
    for _ in range(10):
        driver.execute_script("window.scrollBy(0,10)")
        
        imgs = driver.find_elements(By.XPATH,"//img[@class='rg_i Q4LuWd']")
    img_url = []
    for image in imgs:
        source = image.get_attribute('src')
        if source is not None:
            if(source[0:4] == 'http'):
                img_url.append(source)
    for i in img_url[:10]:
        urls.append(i)
        
for i in range(len(urls)):
    if i >= 50:
        breakBy.XPATH,
    response = requests.get(urls[i])
    print("Downloading {0} of {1} images" .format(i,50))
    file=open(r"C:\Users\NAVEEN\Downloads\New folder"+str(i)+".jpg","wb")
    file.write(response.content)
    


# In[ ]:


4.## a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com##


# In[35]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[36]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[37]:


driver.maximize_window()


# In[38]:


url = "https://www.flipkart.com/"
driver.get(url)


# In[5]:


page=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
page.click()


# In[6]:


search= driver.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('pixel 4A')


# In[7]:


search_button =driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_button.click()


# In[8]:


urls=[]
url=driver.find_elements(By.XPATH,"//a[@class='_1fQZEK']")
for i in url:
    urls.append(i.get_attribute('href'))


# In[9]:


print(len(urls))


# In[12]:


Brand=[]
Name=[]
Colour=[]
RAM=[]
ROM=[]
Primary_Camera=[]
Secondary_Camera=[]
Display_Size=[]
Battery_Capacity=[]
Price=[]
url=[]

for i in urls:
    driver.get(i)
    url.append(i)
    
    try:
        read_more = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _1FH0tX']")
        read_more.click()
    except NoSuchElementException:
        print()
        
    try:
        brand=driver.find_element(By.XPATH,"//span[@class='B_NuCI']")
        Brand.append(brand.text.split()[0])
    except NoSuchElementException:
        Brand.append('-')
        
        
    try:
        name= driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[3]/td[2]/ul/li")
        Name.append(name.text)
    except NoSuchElementException:
        Name.append('-')
        
        
    try:
        color= driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][1]/table/tbody/tr[4]/td[2]/ul/li")
        Colour.append(color.text)
    except NoSuchElementException:
        Colour.append('-')
    
    try:
        ram= driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[2]/td[2]/ul/li")
        RAM.append(ram.text)
    except NoSuchElementException:
        RAM.append('-')
            
    try:
        rom = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][4]/table[1]/tbody/tr[1]/td[2]/ul/li")
        ROM.append(rom.text)
    except NoSuchElementException:
        ROM.append('-')
        
        
    try:
        primary =driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[2]/td[2]/ul/li")
        Primary_Camera.append(primary.text)
    except NoSuchElementException:
        Primary_Camera.append('-')
     
    try:
        secondary=driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][5]/table[1]/tbody/tr[5]/td[2]/ul/li")
        Secondary_Camera.append(secondary.text)
    except NoSuchElementException:
        Secondary_Camera.append('-')
    
    try:
        display = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/div")
        if display.text!= 'Display Features':raise NoSuchElementException
        disp_size = driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][2]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Display_Size.append(disp_size.text)
    except NoSuchElementException:
        Display_Size.append('-')
       
    try:
        battery= driver.find_element(By.XPATH,"//div[@class='_3k-BhJ'][10]/table[1]/tbody/tr[1]/td[2]/ul/li")
        Battery_Capacity.append(battery.text)
    except NoSuchElementException:
        Battery_Capacity.append('-')   
    
    try:
        price= driver.find_element(By.XPATH,"//div[@class='_30jeq3 _16Jk6d']")
        Price.append(price.text)
    except NoSuchElementException:
        Price.append('-')    


# In[13]:


print(len(Brand),len(Name),len(Colour),len(RAM),len(ROM),len(Primary_Camera),len(Secondary_Camera),len(Display_Size),len(Battery_Capacity),len(Price),len(url)) 


# In[14]:


df = pd.DataFrame({'Brand':Brand,'Name':Name,'Colour':Colour,'RAM':RAM,'ROM':ROM,'Primary Camera':Primary_Camera,'Secondary Camera':Secondary_Camera,'Display Size':Display_Size,'Battery':Battery_Capacity,'Price':Price,'URL':url})
df


# In[ ]:


df.to_csv("df.csv")


# In[ ]:


driver.close()


# In[ ]:


5.##Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps. ##


# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import requests
import re
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[2]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[3]:


driver.maximize_window()


# In[4]:


url = 'https://www.google.co.in/maps'
driver.get(url)


# In[5]:


search=driver.find_element(By.XPATH,"//input[@class='searchboxinput xiQnY']")
search.send_keys('Panipat')


# In[6]:


search_button=driver.find_element(By.XPATH,"//button[@class='mL3xi']")
search_button.click()


# In[7]:


try:
    url= driver.current_url
    print(url)
    latitude =re.findall(r'\@(-?[\d\.]*)',url)
    longitude=re.findall(r'\@[-?\d\.]*\,([-?\d\.]*)',url)
    print(latitude)
    print(longitude)
except Exception as e:
    print(str(e))


# In[ ]:


6.##Write a program to scrap all the available details of best gaming laptops from digit.in. ##


# In[36]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[37]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[38]:


driver.maximize_window()


# In[39]:


url = "https://www.digit.in/"
driver.get(url)


# In[40]:


Best_Laptops= driver.find_element(By.XPATH,"//div[@class='listing_container']//ul//li[9]")
Best_Laptops.click()


# In[41]:


Name = []
Operating_System = []
Display = []
Processor = []
Memory = []
Weight = []
Dimensions = []
Graphics_Processor = []
Price = []


# In[42]:


name = driver.find_elements(By.XPATH,"//span[@class='datahreflink']")
for i in name:
    Name.append(i.text)
    
try:
    system = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[1]/div/div")
    for s in system:
        Operating_System.append(s.text)
except NoSuchElementException:
    pass

try:
    display = driver.find_elements(By.XPATH,"//div[@class='product-detail']/div/ul/li[2]/div/div")
    for d in display:
        Display.append(d.text)
except NoSuchElementException:
    pass

try:
    processor = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[4]/td[3]")
    for p in processor:
        Processor.append(p.text)
except NoSuchElementException:
    pass
try:
    memory = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[5]/td[3]")
    for m in memory:
        Memory.append(m.text)
except NoSuchElementException:
    pass

try:
    weight = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[7]/td[3]")
    for w in weight:
        Weight.append(w.text.split('&')[1])
except NoSuchElementException:
    pass

try:
    dimension = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[7]/td[3]")
    for dim in dimension:
        Dimensions.append(dim.text.split('&')[0])
except NoSuchElementException:
    pass

try:
    graphic = driver.find_elements(By.XPATH,"//div[@class='Spcs-details'][1]/table/tbody/tr[6]/td[3]")
    for g in graphic:
        Graphics_Processor.append(g.text)
except NoSuchElementException:
    pass

try:
    price = driver.find_elements(By.XPATH,"//td[@class='smprice']")
    for pr in price:
        Price.append(pr.text.replace('₹ ','Rs'))
except NoSuchElementException:
    pass


# In[43]:


print(len(Name),len(Operating_System),len(Display),len(Processor),len(Memory),len(Weight),len(Dimensions),len(Graphics_Processor),len(Price))


# In[44]:


df=pd.DataFrame({'Name':Name[:7],'Operating System':Operating_System,'Display':Display,'Processor':Processor,'Memory':Memory,'Weight':Weight,'Dimensions':Dimensions,'Graphics Processor':Graphics_Processor,'Price':Price})
df


# In[ ]:


7.## a python program to scrape the details for all billionaires from www.forbes.com##


# In[39]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[40]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[41]:


driver.maximize_window()


# In[42]:


url ="https://www.forbes.com/"
driver.get(url)


# In[43]:


opt_btn = driver.find_element(By.XPATH,"//div[@class='_8FT-x3t4']")
opt_btn.click()


# In[44]:


billionaries= driver.find_element(By.XPATH,"//li[@class='TjJgrPSg cD45ib6e primary']")
billionaries.click()


# In[45]:


World_billionaries = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div/section/div[2]/div/div/div[1]/div/div[1]/div/div/a/h2")
World_billionaries.click()


# In[49]:


Rank=[]
Name = []
Age = []
Citizenship = []
Source = []
Industry = []
Net_Worth = []

try:
    rank = driver.find_elements(By.XPATH,"//div[@class='Table_rank___YBhk Table_dataCell__2QCve']")
    for i in rank:
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append('-')
    
try:
    name = driver.find_elements(By.XPATH,"//div[@class='TableRow_row__L-0Km']/div[2]/div")
    for i in name:
        Name.append(i.text)
except NoSuchElementException:
    Name.append('-')

try:
    age = driver.find_elements(By.XPATH,"//div[@class='TableRow_row__L-0Km']/div[4]/div")
    for i in age:
        Age.append(i.text)
except NoSuchElementException:
    Age.append('-')

try:
    citizenship = driver.find_elements(By.XPATH,"//div[@class='TableRow_row__L-0Km']/div[5]")
    for i in citizenship:
        Citizenship.append(i.text)
except NoSuchElementException:
    Citizenship.append('-')

try:
    source= driver.find_elements(By.XPATH,"//div[@class='Table_dataCell__2QCve']/span")
    for i in source:
        Source.append(i.text)
except NoSuchElementException:
    Source.append('-')

try:
    industry= driver.find_elements(By.XPATH,"//div[@class='TableRow_row__L-0Km']/div[7]")
    for i in industry:
        Industry.append(i.text)
except NoSuchElementException:
    Industry.append('-')

try:
    net_worth= driver.find_elements(By.XPATH,"//div[@class='Table_netWorth___L4R5 Table_dataCell__2QCve']")
    for i in net_worth:
        Net_Worth.append(i.text)
except NoSuchElementException:
    Net_Worth.append('-')


# In[50]:


print(len(Rank),len(Name),len(Age),len(Citizenship),len(Source),len(Industry),len(Net_Worth))


# In[51]:


df=pd.DataFrame({'Rank':Rank,'Name':Name,'Age':Age,'Citizenship':Citizenship,'Source':Source,'Industry':Industry,'Net Worth':Net_Worth})
df


# In[ ]:


8.## a program to extract at least 500 Comments, Comment upvote and time when comment was posted from any YouTube Video##


# In[19]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait


# In[20]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[21]:


driver.maximize_window()


# In[22]:


url = "https://www.youtube.com/"
driver.get(url)


# In[23]:


search= driver.find_element(By.XPATH,"//div[@class='ytd-searchbox-spt']/input")
search.send_keys("omg2")   


# In[24]:


button = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button")
button.click()


# In[25]:


video = driver.find_element(By.XPATH,"//yt-formatted-string[@class='style-scope ytd-video-renderer']")
video.click()


# In[26]:


for _ in range(10000):
    driver.execute_script("window.scrollBy(0,10000)")


# In[27]:


Comments = []
Comments_Time = []
Time = []
Upvote = []
No_of_Upvotes = []

comments = driver.find_elements(By.XPATH,"//yt-formatted-string[@class='style-scope ytd-comment-renderer']")
for i in comments:
    if i.text is None:
        Comments.append("-")
    else:
        Comments.append(i.text)

time = driver.find_elements(By.XPATH,"//yt-formatted-string[@class='published-time-text style-scope ytd-comment-renderer']")
for i in time:
    Time.append(i.text)
    
for i in range(0,len(Time),2):
    Comments_Time.append(Time[i])


upvote = driver.find_elements(By.XPATH,"//span[@class='style-scope ytd-comment-action-buttons-renderer']")
for i in upvote:
    Upvote.append(i.text)
    
for i in range(1,len(Upvote),2):
    No_of_Upvotes.append(Upvote[i])


# In[28]:


print(len(Comments),len(Comments_Time),len(No_of_Upvotes))


# In[29]:


df=pd.DataFrame({'Comments':Comments[:500],'Comments Time':Comments_Time[:500],'Comment Upvotes':No_of_Upvotes[:500]})
df


# In[ ]:


9.## a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in “London” location. ##


# In[53]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


# In[54]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[55]:


driver.maximize_window()


# In[56]:


url = "https://www.hostelworld.com/"
driver.get(url)


# In[57]:


search=driver.find_element(By.XPATH,"//input[@class='native-input body-1-reg']")
search.send_keys('London')


# In[58]:


London = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/ul/li[2]/button")
London.click()


# In[59]:


search_button =driver.find_element(By.XPATH,"//button[@class='btn-content large-button icon-only']")
search_button.click()


# In[60]:


Name = []
Distance=[]
Ratings = []
Reviews = []
Overall_Reviews = []
Description = []
Facilities=[]
Pvt_Prices=[]
Dorms_Prices=[]
urls=[]
  
try:
    name = driver.find_elements(By.XPATH,"//div[@class='property-name']")
    for i in name:
        Name.append(i.text)
except NoSuchElementException:
    Name.append('-')
      
try:
    distance = driver.find_elements(By.XPATH,"//span[@class='distance-description']")
    for i in distance:
        Distance.append(i.text.replace('-',''))
except NoSuchElementException:
    Distance.append('-')
    
try:
    ratings = driver.find_elements(By.XPATH,"//span[@class='number']")
    for i in ratings:
        Ratings.append(i.text)
except NoSuchElementException:
    Ratings.append('-')
        
try:
    reviews = driver.find_elements(By.XPATH,"//div[@class='rating-score']")
    for i in reviews:
        Reviews.append(i.text .replace('\n','')[3:])
except NoSuchElementException:
    Reviews.append('-')
    
try:
    overall_reviews = driver.find_elements(By.XPATH,"//span[@class='left-margin']")
    for i in overall_reviews:
        Overall_Reviews.append(i.text)
except NoSuchElementException:
    Overall_Reviews.append('-')
            
try:
    price = driver.find_elements(By.XPATH,'//div[@class="property-accommodation-price"]')[1::2]
    for i in price:
        Pvt_Prices.append(i.text.replace('\n','').replace('-20%','').replace('Privates From',''))
except NoSuchElementException:
    Pvt_Prices.append('-')
    
try:
    price = driver.find_elements(By.XPATH,"//div[@class='property-accommodation-price']")[0::2]
    for i in price:
        Dorms_Prices.append(i.text.replace('\n',' ').replace('-20% ','').replace('-10% ','').replace('-5% ','').replace('Dorms From ','').replace('From ',''))
except NoSuchElementException:
    Dorms_Prices.append('-')
 
  
url=driver.find_elements(By.XPATH,"//a[@class='property-card-container horizontal']")
for i in url:
    urls.append(i.get_attribute('href'))                           
                           
for i in urls:
    driver.get(i)
        
    
    try:
        description= driver.find_elements(By.XPATH,"//div[@class='description-container']")
        for i in description:
            Description.append(i.text.replace('\n','').replace("Property Description",'').replace('Hostelworld says',''))
    except NoSuchElementException:
        Description.append('-')
     
    
    try:
        fac1 = driver.find_elements(By.XPATH,"//div[@class='page-inner']/div/ul/li[1]/ul/li[1]")
        fac2 = driver.find_elements(By.XPATH,"//div[@class='page-inner']/div/ul/li[1]/ul/li[2]")
        for i in fac1:
            for j in fac2:
                Facilities.append(i.text+','+j.text)
    except NoSuchElementException:
        Facilities.append('-')
     


# In[61]:


print(len(Name),len(Distance),len(Ratings),len(Reviews),len(Overall_Reviews),len(Pvt_Prices),len(Dorms_Prices),len(Description),len(Facilities),len(urls))


# In[64]:


df=pd.DataFrame({'Name':Name[1:31],'Distance':Distance,'Ratings':Ratings[1:31],'Reviews':Reviews[1:31],'Overall Reviews':Overall_Reviews,'Private Prices':Pvt_Prices,'Dorms Price':Dorms_Prices[1:31],'Description':Description[:30],'Facilities':Facilities})
df


# In[ ]:




