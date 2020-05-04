import requests
import json
import pandas as pd
from newsapi.newsapi_client import NewsApiClient
import re

# # Extracting:
newsapi = NewsApiClient(api_key='af7eaa1b2a2f45bfa765b99def007d26')

url1 = newsapi.get_everything(q='Canada',
                                      language='en',
                                      sort_by='relevancy',
                                      page_size=100);
url2 = newsapi.get_everything(q='University',
                                      language='en',
                                      sort_by='relevancy',
                             page_size=100)
url3 = newsapi.get_everything(q='Dalhousie+University',
                                      language='en',
                                      sort_by='relevancy',
                             page_size=100)
url4 = newsapi.get_everything(q='Halifax',
                                      language='en',
                                      sort_by='relevancy',
                             page_size=100)
url5 = newsapi.get_everything(q='Canada+Education',
                                      language='en',
                                      sort_by='relevancy',
                             page_size=100)

url1 = url1['articles']
url2 = url2['articles']
url3 = url3['articles']
url4 = url4['articles']
url5 = url5['articles']

url = url1 + url2 + url3 + url4 + url5

data = json.dumps(url)
data = json.loads(data)

#Cleaning function
def cleaning(inputString):
    inputString = re.sub(r'\[[^\]]*\]','',inputString)
    inputString = re.sub(r'http\S+', '', inputString)
    inputString = re.sub('[^A-Za-z0-9]+',' ', inputString)
    return inputString

for x in range(len(data)):
    data[x]['content'] = cleaning(str(data[x]['content']))

with open('newAPI_Data.json','w') as outfile:
    json.dump(data,outfile,indent=4)