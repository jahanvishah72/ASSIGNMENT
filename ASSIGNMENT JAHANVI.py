#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests

# Making a GET request
r = requests.get('https://www.bls.gov/')

# print request object
print(r.url)

# print status code
print(r.status_code)


# In[3]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.bls.gov/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# In[4]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.bls.gov/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
print(soup.title)

# Getting the name of the tag
print(soup.title.name)

# Getting the name of parent tag
print(soup.title.parent.name)

# use the child attribute to get
# the name of the child tag


# In[9]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.bls.gov/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

images_list = []

images = soup.select('img')
for image in images:
	src = image.get('src')
	alt = image.get('alt')
	images_list.append({"src": src, "alt": alt})
	
for image in images_list:
	print(image)


# In[10]:


import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.bls.gov/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# find all the anchor tags with "href"
for link in soup.find_all('a'):
	print(link.get('href'))

