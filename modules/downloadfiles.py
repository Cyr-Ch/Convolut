from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib
import argparse

def download_pdfs(website, supplier):
    # connect to website and get list of all pdfs
    url=website
    response = request.urlopen(url).read()
    soup= BeautifulSoup(response, "html.parser")     
    links = soup.find_all('a', href=re.compile(r'(.pdf)'))


    # clean the pdf link names
    url_list = []
    for el in links:
        if(el['href'].startswith('http')):
            url_list.append(el['href'])
        else:
            url_list.append(website+"/"+el['href'])

    print(url_list)


    # download the pdfs to a specified location
    os.makedirs(os.path.join("/mnt/c/Users/t-cchaabani/Downloads/Convolut/modules", supplier), exist_ok=True)
    for url in url_list:
        print(url)
        fullfilename = os.path.join(os.path.join("/mnt/c/Users/t-cchaabani/Downloads/Convolut/modules",supplier), url.split("/")[-1])
        #os.makedirs(fullfilename)
        #print(fullfilename)
        if len(fullfilename)> 200:
            url_short = url.split("/")[-1]
            fullfilename = os.path.join(os.path.join("/mnt/c/Users/t-cchaabani/Downloads/Convolut/modules",supplier), url_short[int(5*len(url_short)/6):-1])
        request.urlretrieve(url, fullfilename)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--website", default="", help="Please enter the website of your supplier")
    argparser.add_argument("--supplier", default="", help="Please enter namee of your supplier")
    
    
    args = argparser.parse_args()
    print("Searching and downloading the pdfs on your website: "+ args.website)
    download_pdfs(args.website, args.supplier)