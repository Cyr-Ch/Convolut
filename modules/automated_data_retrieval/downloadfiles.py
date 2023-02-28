import os
import argparse
from constants import RELEVANT_KEYWORDS

def download_pdfs(website):
    #print(website)
    folder_name=website.replace("https://","").replace("http://","").replace("/","")
    os.makedirs(folder_name, exist_ok=True)
    os.system("wget -U chrome -r -l20 --directory-prefix "+folder_name+" --no-parent -A.pdf "+website)
    os.system("wget -U chrome -r -l20 --directory-prefix "+folder_name+" --no-parent -A.html "+website)

        

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--website", default="", help="Please enter the website of your supplier")
    #argparser.add_argument("--supplier", default="", help="Please enter namee of your supplier")
    
    
    args = argparser.parse_args()
    print("Searching and downloading the pdfs on your website: "+ args.website)
    download_pdfs(args.website)#, args.supplier)