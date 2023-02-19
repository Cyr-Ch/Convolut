from urllib import request
from bs4 import BeautifulSoup
import re
import os
import urllib
import requests
import argparse
import glob
import csv
from constants import RELEVANT_KEYWORDS

def download_pdfs(website):
    os.system("wget -U chrome -r -l20 --no-parent -A.pdf "+website)
    os.system("wget -U chrome -r -l20 --no-parent -A.html "+website)

def filter_content(data_dir):
    os.mkdir(os.path.join(data_dir, "file_analysis"), exist_ok=True)
    relevance = {"relevent": [], "non-relevent":[]}
    for file in glob.glob(os.path.join(data_dir, "*.pdf")):
        if file.lower() in RELEVANT_KEYWORDS:
            relevance["relevent"].append(file)
        else:
            relevance["non-relevent"].append(file)

    with open (os.path.join(data_dir, "file_analysis", "filtered_files.csv"), "w") as f:  
        w = csv.DictWriter(f, relevance.keys())
        w.writeheader()
        w.writerow(relevance)


        

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--website", default="", help="Please enter the website of your supplier")
    #argparser.add_argument("--supplier", default="", help="Please enter namee of your supplier")
    
    
    args = argparser.parse_args()
    print("Searching and downloading the pdfs on your website: "+ args.website)
    download_pdfs(args.website)#, args.supplier)