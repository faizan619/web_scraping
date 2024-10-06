import requests
from bs4 import BeautifulSoup
import json

url = "https://faizanalam.tech"

req = requests.get(url)

if(req.status_code == 200):
    paring = req.text
else:
    print('Access Denied of the Site : ',url)
    
    
soup = BeautifulSoup(paring,'lxml')
if(soup):
    links = soup.find_all('a')
    # print(links,'\n')
    
    link_data = []
    for link in links:
        # print(link['href'])
        url = link['href']
        # print(link.text)
        name = link.text
        # print(f'Name : {name} \nURL : {url}\n')
        link_data.append({
            "name": name,
            "url": url
        })
    with open('links.json', 'w') as json_file:
        json.dump(link_data, json_file, indent=4)
    print(json.dumps(link_data,indent=2))
    print("Data written to links.json")
else:
    print('No data have been found!')

