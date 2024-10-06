import requests
from bs4 import BeautifulSoup

def Auction(url):
    # print("Url :",url)
    response = requests.get(url)
    if (response.status_code == 200):
        parsing = response.text
    else:
        print("Access Denied to Crawl The URL : ",url)
        parsing = ""
    
    soup = BeautifulSoup(parsing,'lxml')
    if (soup):
        section = soup.find_all('section',class_ = "ih-points-table-sec position-relative")
        # print(section)
        for sect in section:
            teamName = sect.find('h2')
            print(teamName.text)

    else:
        print('Crawling Stopped')
    

url = "https://www.iplt20.com/auction/2023"
fetch_data = Auction(url)