The Prototype consists of several PoCs that were developed to test the feasibility of the features
proposed in Konvolut, namely: Automated Supplier Search, Web Scraping, Text Sentiment Analysis and the Solid Pods Technology. The focus of the development was set on the Text Sentiment
Analysis and Solid Pods components, as they are known to be the most challenging aspects of Konvolut.

While all of the PoCs are coded in python, they do have different requirements in terms of libraries,
hardware requirements (storage and computation) as well as the platforms in which they could
be tested. Moreover, the Solid Pods PoC uses node.js, html and java script on top of the python
scripts.

The PoCs are developed in two different branches of the same repository to avoid any confusions and keep a good overview on each seperate feature. The branches are named according the task that they accomplish, namely:
1. Webscraping: This branch contains all of the code related to supplier search, retrieval of
data and the classification of the sentiment occurring in text data (several methods are tested
and compared).
2. Solidpods: In this branch, the PoC for managing and uploading data to a solid pod server
is developed. These tasks can be performed using the User interface provided within the
branch.
