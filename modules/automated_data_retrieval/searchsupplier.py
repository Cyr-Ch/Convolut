import argparse
from googlesearch import search
from downloadfiles import download_pdfs
from classifyfiles import filter_content


def google_search(query):
    results = search(query, num_results=10)
    relevant_web = []
    for result in results:
        if query.lower() in result:
            relevant_web.append(result)
    if len(relevant_web) == 0:
        print("Supplier does not seem to have an official website under this name, please try a different one (abbreviation, etc)")
    else:
        print("The following websites were found:")
        for s in relevant_web:
            if query.lower() in s:
                print(s+" : seems to be very relevant")
            else:
                print(s)
    return relevant_web



if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--supplier", default="", help="Please enter the name of your supplier")
    
    
    args = argparser.parse_args()
    print("running a google search on your supplier: "+ args.supplier)
    relevant_web = google_search(args.supplier)

    print("Downloading data from relevant websites")
    #for web in relevant_web:
    #    download_pdfs(web)

    for web in relevant_web:
        #print(web)
        filter_content(web)