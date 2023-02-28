import os
import argparse
import glob
import csv
from constants import RELEVANT_KEYWORDS


def filter_content(data_dir):
    folder_name=data_dir.replace("https://","").replace("http://","").replace("/","")
    if os.path.exists(folder_name):
        os.makedirs(os.path.join(folder_name, "file_analysis"), exist_ok=True)
        relevance = {"relevant": [], "non-relevant":[]}
        for file in glob.glob(os.path.join(folder_name, "/**/*.pdf")):
            print("looking into file")
            print(file)
            if file.lower() in RELEVANT_KEYWORDS:
                relevance["relevant"].append(file)
            else:
                relevance["non-relevant"].append(file)
        for file in glob.glob(os.path.join(folder_name, "/**/*.html")):
            print("looking into file")
            print(file)
            if file.lower() in RELEVANT_KEYWORDS:
                relevance["relevant"].append(file)
            else:
                relevance["non-relevant"].append(file)

        with open (os.path.join(folder_name, "file_analysis", "filtered_files.csv"), "w") as f:  
            w = csv.DictWriter(f, relevance.keys())
            w.writeheader()
            w.writerow(relevance)


        

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--datadir", default="", help="Please enter directory of your data")
    #argparser.add_argument("--supplier", default="", help="Please enter namee of your supplier")
    
    
    args = argparser.parse_args()
    print("Searching and downloading the pdfs on your website: "+ args.website)
    filter_content(args.datadir)