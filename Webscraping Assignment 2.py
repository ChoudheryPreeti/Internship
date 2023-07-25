#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install selenium')


# In[ ]:


##1.e a python program to scrape data for “Data Analyst” Job position in “Bangalore” location.##


# In[63]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[64]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[65]:


driver.maximize_window()


# In[66]:


url='http://www.naukri.com'
driver.get(url)


# In[67]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Analyst")


# In[68]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("bangalore")


# In[69]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[70]:


job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[71]:


job_location=[]
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[72]:


company_name=[]
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[73]:


experience_required=[]
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[74]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[75]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company Name':company_name,'Experience':experience_required})
df


# In[ ]:


2.## a python program to scrape data for “Data Scientist” Job position in “Bangalore” location##


# In[76]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[77]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[78]:


driver.maximize_window()


# In[79]:


url='http://www.naukri.com'
driver.get(url)


# In[80]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Scientist")


# In[81]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("bangalore")


# In[82]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[83]:


job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[84]:


job_location1=[]
location1_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location1_tags[0:10]:
    location1=i.text
    job_location1.append(location1)


# In[85]:


company_name=[]
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[86]:


print(len(job_title),len(job_location1),len(company_name))


# In[87]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location1,'Company Name':company_name})
df


# In[ ]:


3.##scrape data  for “Data Scientist” designation for first 10 job results.You have to scrape the job-title, job-location, company name, experience required. The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs##


# In[394]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[395]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[396]:


driver.maximize_window()


# In[397]:


url='http://www.naukri.com'
driver.get(url)


# In[136]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Scientist")


# In[137]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys("Delhi/NCR")


# In[138]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[140]:


loc_filter=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft filterLabel"]')
for i in loc_filter :
    if (i.text=='Delhi / NCR'):
        i.click()
        break


# In[141]:


sal_filter=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft filterLabel"]')
for i in sal_filter:
    if(i.text=='3-6 Lakhs'):
        i.click()
        break


# In[142]:


job_title=[]
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[143]:


job_location1=[]
location1_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location1_tags[0:10]:
    location1=i.text
    job_location1.append(location1)


# In[144]:


company_name=[]
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[145]:


experience_required=[]
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[146]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location1,'Company Name':company_name,'Experience':experience_required})
df


# In[ ]:


4.##Scrape data of first 100 sunglasses listings on flipkart.com##


# In[20]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[21]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[22]:


driver.maximize_window()


# In[23]:


url='http://www.flipkart.com'
driver.get(url)


# In[24]:


page=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
page.click()


# In[25]:


search= driver.find_element(By.CLASS_NAME,'_3704LK')
search.send_keys('sunglasses')


# In[26]:


search_button =driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_button.click()


# In[27]:


Brand = []
for i in range(3):
    brand = driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in brand:
        Brand.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[28]:


print(len(Brand))


# In[33]:


Product_DES = []
for i in range(3):
    product = driver.find_elements(By.XPATH,"//a[@class='IRpwTa']")
    for i in product:
        Product_DES.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[34]:


print(len(Product_DES))


# In[35]:


Price= []
for i in range(3):
    price = driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")
    for i in price:
        Price.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[36]:


print(len(Price))


# In[37]:


df = pd.DataFrame({'Brand': Brand,'Product Description':Product_DES,'Price':Price})
df[0:100]


# In[ ]:


5.##Scrape 100 reviews data from flipkart.com for iphone11 phone##


# In[214]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[215]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[216]:


driver.maximize_window()


# In[217]:


url='https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART%2F&page=1'
driver.get(url)


# In[229]:


Rating= []
for i in range(10):
    rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating:
        Rating.append(i.text)
Rating
next_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
next_button.click()


# In[230]:


print(len(Rating))


# In[234]:


Review_Summary = []
for i in range(10):
    review_summary= driver.find_elements(By.XPATH,"//p[@class='_2-N8zT']")
    for i in review_summary:
        Review_Summary.append(i.text)
Review_Summary  
next_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
next_button.click()


# In[235]:


print(len(Review_Summary))


# In[236]:


Full_Review=[]
for i in range(10):
    full_review=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review:
        Full_Review.append(i.text)
Full_Review
next_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
next_button.click()


# In[237]:


print(len(Full_Review))


# In[238]:


df=pd.DataFrame({'Rating':Rating,'Review Summary':Review_Summary,'Full Review':Full_Review})
df


# In[ ]:


6.##Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.##


# In[38]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[39]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[40]:


driver.maximize_window()


# In[42]:


url='https://www.flipkart.com/'
driver.get(url)


# In[43]:


page2=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
page2.click()


# In[44]:


search1= driver.find_element(By.CLASS_NAME,'_3704LK')
search1.send_keys('sneakers')


# In[45]:


search_button1=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_button1.click()


# In[46]:


Brand= []
for i in range(3):
    brand = driver.find_elements(By.XPATH,"//div[@class='_2WkVRV']")
    for i in brand:
        Brand.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[47]:


print(len(Brand))


# In[48]:


Product_DES = []
for i in range(3):
    product = driver.find_elements(By.XPATH,"//div[@class='_2B099V']")
    for i in product:
        Product_DES.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[49]:


print(len(Product_DES))


# In[50]:


Price= []
for i in range(3):
    price = driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")
    for i in price:
        Price.append(i.text)
        
nxt_button=driver.find_element(By.XPATH,"//a[@class='_1LKTO3']")
nxt_button.click()


# In[51]:


print(len(Price))


# In[53]:


df = pd.DataFrame({'Brand': Brand,'Product Description':Product_DES,'Price':Price})
df[0:100]


# In[ ]:


7.##: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7”##


# In[54]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[55]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[56]:


driver.maximize_window()


# In[57]:


url='http://www.amazon.in/'
driver.get(url)


# In[ ]:


search3= driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search3.send_keys('laptop')


# In[58]:


search_button3=driver.find_element(By.XPATH,'//span[@class="nav-search-submit-text nav-sprite nav-progressive-attribute"]')
search_button3.click()


# In[59]:


Title=[]
title=driver.find_elements(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
for i in title[:10]:
    Title.append(i.text)
Title


# In[60]:


## Rating part needs to be skipped as told##


# In[61]:


Price=[]
price=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
for i in price[:10]:
    Price.append(i.text)
Price


# In[62]:


df=pd.DataFrame({'Title':Title,'Price':Price})
df


# In[ ]:


8.## a python program to scrape data for Top 1000 Quotes of All Time##


# In[63]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[64]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[65]:


driver.maximize_window()


# In[66]:


url='http://www.azquotes.com/'
driver.get(url)


# In[67]:


Top=[]
top=driver.find_elements(By.XPATH,"//a[@class='title']")
for i in top:
    Top.append(i.text)
Top


# In[68]:


print(len(Top))


# In[69]:


Author=[]
author=driver.find_elements(By.XPATH,"//div[@class='author']")
for i in author:
    Author.append(i.text)
Author


# In[70]:


print(len(Author))


# In[71]:


Type_of_quote=[]
type_of_quote=driver.find_elements(By.XPATH,"//div[@class='tags']")
for i in type_of_quote[0:1001]:
    Type_of_quote.append(i.text)
Type_of_quote


# In[72]:


print(len(Type_of_quote))


# In[73]:


df=pd.DataFrame({'Top':Top,'Authors':Author,'Type of Quote':Type_of_quote})
df


# In[ ]:


9.##Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, Term of office, Remarks) ##


# In[90]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[91]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[92]:


driver.maximize_window()


# In[93]:


url='http://www.jagranjosh.in/'
driver.get(url)


# In[94]:


Name=[]
name=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[2]/p')
for i in name:
    Name.append(i.text)
Name


# In[95]:


Born_Dead=[]
born_dead=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[3]/p')
for i in born_dead:
    Born_Dead.append(i.text)
Born_Dead


# In[96]:


Term_of_Office=[]
term_of_Office=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[4]/p')
for i in term_of_Office:
    Term_of_Office.append(i.text)
Term_of_Office


# In[97]:


n=len(Term_of_Office)
k=19
for i in range(0,n-k):
    Term_of_Office.pop()


# In[98]:


Remarks=[]
remarks=driver.find_elements(By.XPATH,'//div[@class="table-box"]/table/tbody/tr/td[5]/p')
for i in remarks:
    Remarks.append(i.text)
Remarks


# In[99]:


print(len(Name),len(Born_Dead),len(Term_of_Office),len(Remarks))


# In[100]:


df=pd.DataFrame({'Name':Name,'Born-Dead':Born_Dead,'Term Of Office':Term_of_Office,'Remarks':Remarks})
df


# In[ ]:


10.##Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price)##


# In[239]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[240]:


driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[241]:


driver.maximize_window()


# In[242]:


url='http://www.motor1.com'
driver.get(url)


# In[244]:


Name=[]
name=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in name:
    Name.append(i.text)
Name


# In[245]:


print(len(Name))


# In[247]:


Price=[]
price=driver.find_elements(By.XPATH,'//strong')
for i in price:
    Price.append(i.text)
Price


# In[248]:


print(len(Price))


# In[250]:


df=pd.DataFrame({'Name':Name,'Price':Price})
df[0:50]


# In[ ]:




