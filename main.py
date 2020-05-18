import requests
from bs4 import BeautifulSoup
import sys

def search(s):
    
    # use the user's search term to create a requests from bing.com
    params = {'q': s}
    r = requests.get('https://www.bing.com/search', params=params)


    #parse it into BeautifulSoup to get the required html elements
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find("ol", {'id': 'b_results'})
    links = results.findAll("li", {'class': 'b_algo'})
    if links:
        print("\n\n")
    #print the required html elements from the BeautifulSoup Object
    for link in links:
        link_title = link.find("a").text
        link_href = link.find("a").attrs["href"]
        link_content = link.find("p").text

        if link_title:
            print(link_title)
        if link_href:
            print(link_href)
        if link_content:
            print(link_content)
        print("-------------------------------------------------------------------------------------------------------------------\n")
    if not links:
        search(s)
    else:
        sys.exit(0)

users_search = input('What are you searching for today? ')
search(users_search)
